#lang racket

;; expressions

(define (const? t)
  (number? t))

(define (op? t)
  (and (list? t)
       (member (car t) '(+ - * /))))

(define (op-op e)
  (car e))

(define (op-args e)
  (cdr e))

(define (op-cons op args)
  (cons op args))

(define (op->proc op)
  (cond [(eq? op '+) +]
        [(eq? op '*) *]
        [(eq? op '-) -]
        [(eq? op '/) /]))

(define (let-def? t)
  (and (list? t)
       (= (length t) 2)
       (symbol? (car t))))

(define (let-def-var e)
  (car e))

(define (let-def-expr e)
  (cadr e))

(define (let-def-cons x e)
  (list x e))

(define (let? t)
  (and (list? t)
       (= (length t) 3)
       (eq? (car t) 'let)
       (let-def? (cadr t))))

(define (let-def e)
  (cadr e))

(define (let-expr e)
  (caddr e))

(define (let-cons def e)
  (list 'let def e))

(define (var? t)
  (symbol? t))

(define (var-var e)
  e)

(define (var-cons x)
  x)

(define (arith/let-expr? t)
  (or (const? t)
      (and (op? t)
           (andmap arith/let-expr? (op-args t)))
      (and (let? t)
           (arith/let-expr? (let-expr t))
           (arith/let-expr? (let-def-expr (let-def t))))
      (var? t)))

;; let-lifted expressions

(define (arith-expr? t)
  (or (const? t)
      (and (op? t)
           (andmap arith-expr? (op-args t)))
      (var? t)))

(define (let-lifted-expr? t)
  (or (and (let? t)
           (let-lifted-expr? (let-expr t))
           (arith-expr? (let-def-expr (let-def t))))
      (arith-expr? t)))

;; generating a symbol using a counter
;; renaming vars
(define (number->symbol i)
  (string->symbol (string-append "x" (number->string i))))

(define (indexing v env)
  (define (helper i env)
    (if (null? env) i
           (helper (+ 1 i) (cdr env))))
  (helper 0 env))

(define (find-index var env)
           (if (eq? (caar env) var) (cadar env)
               (find-index var (cdr env))))


(define (change-vars e)
  (define (rename-with-counter t env)
    (define (rename-construct expr env)
      (cons expr env))
    (cond [(const? t) (rename-construct t env)]
          [(var? t)
           (define in-env-ind (find-index t env))
           (define var-with-ind (number->symbol in-env-ind))
         
           (rename-construct var-with-ind env)]
          [(op? t)
           (define first-env (rename-with-counter (cadr t) env))
           (define second-env (rename-with-counter (caddr t) (cdr first-env)))
         
           (rename-construct (list (op-op t) (car first-env) (car second-env))
                             (cdr second-env))]
          [(let? t) (let* ((v (let-def-var (let-def t)))
                           (counter (indexing v env))
                           (v-with-index (number->symbol counter ))
                           (dfexpr-env (rename-with-counter (let-def-expr (let-def t))
                                                            (add-to-env v counter env)))
                           (expr-env (rename-with-counter (let-expr t)
                                                          (add-to-env v counter env))))
                      (rename-construct (let-cons (list v-with-index (car dfexpr-env))
                                                  (car expr-env))
                                        (cdr expr-env)))]))
  (car (rename-with-counter e empty-env)))

;; environments (could be useful for something)

(define empty-env
  null)

(define (add-to-env x v env)
  (cons (list x v) env))

(define (find-in-env x env)
  (cond [(null? env) (error "undefined variable" x)]
        [(eq? x (caar env)) (cadar env)]
        [else (find-in-env x (cdr env))]))

;; the let-lift procedure

;;procedury pomocnicze:

;;nowa struktura pomocnicza:

(define (final-list df ar)
  (cons df (cons ar null)))

;;selektory definicji i wyrażeń arytmetycznych:

(define (defs expr)
  (car expr))

(define (arith expr)
  (cadr expr))

;;wyciąganie let na zewnątrz:

(define (toplevel-let expr)
  (cond [(or (const? expr) (var? expr)) (final-list '() expr)]
        [(op? expr) (let* ((e1 (toplevel-let (cadr expr)))
                           (e2 (toplevel-let (caddr expr)))
                           (ds1 (defs e1))
                           (ds2 (defs e2))
                           (operator (op-op expr))
                           (a1 (arith e1))
                           (a2 (arith e2)))
                      (final-list (append ds1 ds2) (list operator a1 a2)))]
        [(let? expr)
         (define top-let-expr (toplevel-let (let-expr expr)))
         (define top-let-def-expr (toplevel-let (let-def-expr (let-def expr))))
         (define definition (list (let-def-var (let-def expr))
                                  (arith top-let-def-expr)))
         
         (final-list (append (defs top-let-def-expr)
                             (append (defs top-let-expr) definition))
                     (arith top-let-expr))]))

;;właściwa funkcja let-lift
       
(define (let-lift e)
  
  (define (create-result dfs ars)
  (if (null? dfs) ars
      (let-cons (list (car dfs) (cadr dfs))
                (create-result (cddr dfs) ars))))
  
  (define topped-expr (toplevel-let (change-vars e)))
  
  (create-result (defs topped-expr) (arith topped-expr)))


;;testowanie

;;przykłady z tekstu pracowni:
(display "let-lifting dla  (+ 10 (* (let (x 7) (+ x 2)) 2)))")
(newline)
(let-lift '(+ 10 (* (let (x 7) (+ x 2)) 2)))

(display "let-lifting dla (let (x (- 2 (let (z 3) z ))) (+ x 2))")
(newline)
(let-lift '(let (x (- 2 (let (z 3) z ))) (+ x 2)))

(display "let-lifting dla (+ (let (x 5) x) (let (x 1) x))")
(newline)
(let-lift '(+ (let (x 5) x) (let (x 1) x)))


;;własne przykłady:
(display "let-lifting dla (let (x (let (x (let (x 10) x)) x)) x)")
(newline)
(let-lift '(let (x (let (x (let (x 10) x)) x)) x))

(display "let-lifting dla (let (y (let (z (+ (let (x 2) (+ x 1)) 5)) (- z 1))) (* y 2))")
(newline)
(let-lift '(let (y (let (z (+ (let (x 2) (+ x 1)) 5)) (- z 1))) (* y 2)))

(display "let-lifting dla (let (x 7) x)")
(newline)
(let-lift '(let (x 7) x))

(display "let-lifting dla (let (x (* 2 (let (s (+ 2 3)) (+ s 1)))) x)")
(newline)
(let-lift '(let (x (* 2 (let (s (+ 2 3)) (+ s 1)))) x))



;;w powyższym rozwiązaniu nie uwzględniłam wieloargumentowości operacji, są zatem binarne,
;;zgodnie z informacją Profesora Piróga.
;;przy współpracy z Sebastianem Kondraciuk



