#lang racket

;; pomocnicza funkcja dla list tagowanych o określonej długości

(define (tagged-tuple? tag len p)
  (and (list? p)
       (= (length p) len)
       (eq? (car p) tag)))

(define (tagged-list? tag p)
  (and (pair? p)
       (eq? (car p) tag)
       (list? (cdr p))))

;;
;; WHILE
;;


;;dla stanu :

(define (res v s)
  (cons v s))

(define (res-val r)
  (car r))

(define (res-state r)
  (cdr r))

; memory

(define empty-mem
  null)

(define (set-mem x v m)
  (cond [(null? m)
         (list (cons x v))]
        [(eq? x (caar m))
         (cons (cons x v) (cdr m))]
        [else
         (cons (car m) (set-mem x v (cdr m)))]))

(define (get-mem x m)
  (cond [(null? m) 0]
        [(eq? x (caar m)) (cdar m)]
        [else (get-mem x (cdr m))]))

; arith and bool expressions: syntax and semantics

(define (const? t)
  (number? t))

(define (true? t)
  (eq? t 'true))

(define (false? t)
  (eq? t 'false))

(define (op? t)
  (and (list? t)
       (member (car t) '(+ - * / = > >= < <= not and or mod rand))))

(define (op-op e)
  (car e))

(define (op-args e)
  (cdr e))

(define (op->proc op)
  (cond [(eq? op '+) +]
        [(eq? op '*) *]
        [(eq? op '-) -]
        [(eq? op '/) /]
        [(eq? op '=) =]
        [(eq? op '>) >]
        [(eq? op '>=) >=]
        [(eq? op '<)  <]
        [(eq? op '<=) <=]
        [(eq? op 'not) not]
        [(eq? op 'and) (lambda x (andmap identity x))]
        [(eq? op 'or) (lambda x (ormap identity x))]
        [(eq? op 'mod) modulo]
        [(eq? op 'rand) (lambda (max) (min max 4))])) ; chosen by fair dice roll.
                                                      ; guaranteed to be random.

(define (var? t)
  (symbol? t))




;;stary ewaluator wyrażeń arytmetycznych
(define (eval-arith e m)
  (cond [(true? e) true]
        [(false? e) false]
        [(var? e) (get-mem e m)]
        [(op? e)
         (apply
          (op->proc (op-op e))
          (map (lambda (x) (eval-arith x m))
               (op-args e)))]
        [(const? e) e]))





;;eval-arith z dodanym stanem:

(define (new-eval-arith e m st)

  (define (do-op-with-all args acc)
  (if (null? args) acc
      (let ((before (new-eval-arith (car args) m (res-state acc))))
        (do-op-with-all (cdr args) (res ((op->proc (op-op e))
                                         (res-val acc)
                                         (res-val before))
                                        (res-state before))))))

(define (special-forms args acc p)
  (if (or (null? args) (p (res-val acc))) acc
      (let ((before (new-eval-arith (car args) m (res-state acc))))
        (special-forms (cdr args) (res ((op->proc (op-op e)) (res-val acc)
                                                             (res-val before))
                                       (res-state before)) p))))
  (cond ;;wartości boolowskie:
    [(true? e) (res true st)]
    [(false? e) (res false st)]
    ;;stałe:
     [(const? e) (res e st)]
    ;;zmienne:
     [(var? e) (res (get-mem e m) st)]
    ;;obsługa rand:
     [(rand? e) (let ((pair (new-eval-arith (cadr e) m st)))
                  ((rand (res-val pair)) (res-state pair)))]
    ;;operacje:
     [(op? e) (let ((len (length e)))
                (cond [(= 0 len) (res ((op->proc (op-op e))) st)]
                      [(= 1 (length (cdr e))) (let ((pair (new-eval-arith (cadr e) m st)))
                                         (res ((op->proc (op-op e)) (res-val pair)) (res-state pair)))]
                      [else (let ((oper (op-op e))
                                  (args (cddr e))
                                  (acc (new-eval-arith (cadr e) m st))
                                  (yes? (lambda (s) (eq? s #t)))
                                  (no? (lambda (s) (eq? s #f))))
                              (cond [(eq? oper 'and) (special-forms args acc no?)]
                                    [(eq? oper 'or) (special-forms args acc yes?)]
                                    [else    (do-op-with-all args acc)]))]))]))
      
   
;; syntax of commands

(define (assign? t)
  (and (list? t)
       (= (length t) 3)
       (eq? (second t) ':=)))

(define (assign-var e)
  (first e))

(define (assign-expr e)
  (third e))

(define (if? t)
  (tagged-tuple? 'if 4 t))

(define (if-cond e)
  (second e))

(define (if-then e)
  (third e))

(define (if-else e)
  (fourth e))

(define (while? t)
  (tagged-tuple? 'while 3 t))

(define (while-cond t)
  (second t))

(define (while-expr t)
  (third t))

(define (block? t)
  (list? t))


;; psedo-random generator

(define initial-seed
  123456789)

(define (rand max)
  (lambda (i)
    (let ([v (modulo (+ (* 1103515245 i) 12345) (expt 2 32))])
      (res (modulo v max) v))))

(define (rand? t)
  (tagged-tuple? 'rand 2 t))

;; WHILE interpreter

(define (old-eval e m)
  (cond [(assign? e)
         (set-mem
          (assign-var e)
          (eval-arith (assign-expr e) m)
          m)]
        [(if? e)
         (if (eval-arith (if-cond e) m)
             (old-eval (if-then e) m)
             (old-eval (if-else e) m))]
        [(while? e)
         (if (eval-arith (while-cond e) m)
             (old-eval e (old-eval (while-expr e) m))
             m)]
        [(block? e)
         (if (null? e)
             m
             (old-eval (cdr e) (old-eval (car e) m)))]))


;;nowy ewaluator, który pozwala na uzyskiwanie wyników postaci:
;;(wynik-wyrażenia . stan)


(define (new-eval e m st)
  (cond [(assign? e) (let ((pair (new-eval-arith (assign-expr e) m st)))
                       (res (set-mem (assign-var e) (res-val pair) m)
                            (res-state pair)))]
        [(if? e) (let ((pair (new-eval-arith (if-cond e) m st)))
                   (if (res-val pair)
                       (new-eval (if-then e) m (res-state pair))
                       (new-eval (if-else e) m (res-state pair))))]
        [(while? e) (let ((pair (new-eval-arith (while-cond e) m st)))
                      (if (not (res-val pair))
                          (res m (res-state pair))
                          (let (( memst (new-eval (while-expr e) m (res-state pair))))
                            (new-eval e (res-val memst) (res-state memst)))))] 
        [(block? e) (if (null? e) (res m st)
                        (let (( memst (new-eval (car e) m st)))
                          (new-eval (cdr e) (res-val memst) (res-state memst))))]))
      
(define (eval e m seed) (old-eval e m))

(define (run e)
  (new-eval e empty-mem initial-seed))

;;

(define fermat-test
  '( (composite := false); ustawiam wartość zmiennej początkowej na fałsz
         (while (> k 0)  ;aż do momentu, w którym mam licznik > 0 
                ( (exp := (rand (- n 2))) ;;losowanie jakiejś liczby z przedziału 2 --(n-2)
                  (a := (+ 2 exp))
                  (pot := (- n 1))   
                  (res := 1)         ;res to wynik potęgowania
                  ;wykonuję : res*a tak długo aż nie dostanę a^(n-1)
                  (while (> pot 0)
                         ( (res := (* res a))
                           (pot := (- pot 1))))
                  ;właściwy test: sprawdzam czy a^(n-1) dzieli się bez reszty przez n
                  ;   -> TAK: n nie jest liczbą pierwszą
                  ;   -> NIE: kolejny obrót pętli while
                  (if (= (mod (- res 1) n) 0) () 
                      (composite := true))
                  (k := (- k 1)) ))))

(define (probably-prime? n k) ; check if a number n is prime using
                              ; k iterations of Fermat's primality
                              ; test
  (let ([memory (set-mem 'k k
                (set-mem 'n n empty-mem))])
    (not (get-mem
           'composite
         (res-val (new-eval fermat-test memory initial-seed))))))


;;testy do pracowni A
; test A

(display "liczby pierwsze")
(newline)
(and
 (probably-prime? 3 2) 
 (probably-prime? 5 4) 
 (probably-prime? 7 6)
 (probably-prime? 97 95)
 (probably-prime? 23 20)
 (probably-prime? 11 10)
 (probably-prime? 53 50)
 (probably-prime? 79 78)
 (probably-prime? 61 76)
 (probably-prime? 1721 150)
 (probably-prime? 2251 200))
(newline)


(display "liczby zlozone")
(newline)

(define (test)
  (and
   (eq? (probably-prime? 12 14) #f)
   (eq? (probably-prime? 62 15) #f)
   (eq? (probably-prime? 38 15) #f)
   (eq? (probably-prime? 20000 15) #f)
   (eq? (probably-prime? 940 20) #f)
   (eq? (probably-prime? 225 15) #f)
   (eq? (probably-prime? 9 8) #f)
   (eq? (probably-prime? 16 15) #f)
   (eq? (probably-prime? 44 20) #f)
   (eq? (probably-prime? 63 20) #f)
   (eq? (probably-prime? 99 15) #f)))


(test)


;; przez słabej jakości generator liczb pseudolosowych program nie działa dla liczb < 7
;; po zrobieniu zadania B działa juz poprawnie
;;(probably-prime? 5 10) ;; powinno dać #t
;;(probably-prime? 3 10) ;; powinno dać #t



;;testy do pracowni B:

(displayln "czy dla 3 i 5 już działa?")
(define (test1)
  (and (eq? (probably-prime? 3 15) #t)
       (eq? (probably-prime? 5 15) #t)
       (eq? (probably-prime? 7 15) #t)))

(test1)


(define (test2)
  (run '( (x := (+ (rand 10) (rand 10)))))) ;powinno dać wynik 9

(test2)

(define (test3)
  (run '( (x := (rand (rand 7)))
          (y := (rand (rand 7)))
          (z := (+ x y))))) ;;powinno dać wynik 6
(test3)

(define (test4)
  (run '( (x := (and true false))       ;#f
          (y := (and true true))        ;#t
          (z := (or true false))        ;#t
          (p := (or true (/ 1 0)))      ;#t
          (r := (and false (/ 1 0)))))) ;#f

(test4)


(define test7
  '{(a := (rand 20))
    (b := (rand 20))
    (c := (rand 20))
    (d := (rand 20))
    (e := (rand 20))})
 (run test7)

(define (randtest)
  (define a
    (run
     '{(a := (rand 10))
       (b := (rand 10))}))
  (define b
    (run
     '{(a := (+ 2 (rand 20)))
       (b := (+ 2 (rand 20)))}))
  (define x
    (run '{(x := (rand 100))}))
  (define y
    (run '{(x := (rand 100))
           (x := (rand 100))}))
  (let ((aa (get-mem 'a (car a)))
        (ab (get-mem 'b (car a)))
        (ba (get-mem 'a (car b)))
        (bb (get-mem 'b (car b)))
        (xx (get-mem 'x (car x)))
        (xy (get-mem 'x (car y))))
    (and (not (eq? aa ab))
         (not (eq? ba bb))
         (not (eq? xx xy)))))
(display "czy rand działa poprawnie")
(newline)
(randtest)
(newline)

;;zadanie B było konsultowane z Sebastianem Kondraciuk,
;;testy do zadań pisane wspólnie z Julią Nowogrodzką
