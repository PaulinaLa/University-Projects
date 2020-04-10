#lang racket

(define (square x) (* x x))


  
;; główna funkcja do obliczania ułamków łańcuchowych
(define (approximation N D)
  
  (define (iterf fk-1 Ak-1 Ak-2 Bk-1 Bk-2 k) ;; funckja iteracyjna
    ;; warunki na An i Bn 
    (define Ak (+ (* (D k) Ak-1)
                  (* (N k) Ak-2)))
    
    (define Bk (+ (* (D k) Bk-1)
                  (* (N k) Bk-2)))
    
    ;; sposób przybliżania podany w treści zadania
    (define fk (/ Ak Bk))
    
    ;; funkcja która sprawdza czy przybliżenia są dostatecznie blisko siebie
    (define (good-enough? x y)
      (< (abs (- x y)) 0.000001))
    
    (cond
      [(good-enough? fk-1 fk) fk]
      [else           (iterf fk Ak Ak-1 Bk Bk-1 (+ k 1))]))

  (iterf 0 0 1 1 0 1))
;; na początku fk-1 musi być zerem,
;; z treści zadania Ak-1 = 0, Ak-2 = 1 analogicznie w Bk. 


;;TESTY
 ;; przybliżanie arctg(x) 
(define (arctg x)
  (define (num n) (square (* x n)))
  (define (den n) (+ (* 2 n) 1))

  (/ x (+ 1.0 (approximation num den))))

;;przybliżenie π
(define (π)
  (+ 3 (approximation (λ (n) (square (- (* 2 n) 1.0)))
                      (λ (n) 6.0))))
;;przybliżanie tg(x)

(define (tg x)
  
  (define (num n)(- (square x)))
  (define (den n) ( + (* 2 n ) 1))

  (/ x (+ 1.0 (approximation num den))))

;; porównanie z funkcjami wbudowanymi i wartością π

(arctg 5)
(atan 5)
;; π ≈ 3.14159265359...
(π)
(tg 5)
(tan 5)





