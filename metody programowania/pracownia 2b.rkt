#lang racket

(define (average-damp f)
  (lambda (x) (/ (+ x (f x)) 2)))
 
(define (dist x y)
  (abs (- x y)))
 
(define (close-enough? x y)
  (< (dist x y) 0.00001))
 
(define (fix-point f x0)
  (let ((x1 (f x0)))
    (if (close-enough? x0 x1)
        x0
        (fix-point f x1))))
 
 
(define (compose f g)
  (lambda (x) (f (g x))))
 
(define (repeated p n)
  (if (< n 1)
      (λ (x) x)
      (compose p (repeated p (- n 1)))))

;; dla pierwiastka 2-st --> jednokrotne tłumienie
;; dla pierwiastka 3-st --> jednokrotne tłumienie
;; dla pierwiastka 4-st --> dwukrotne tłumienie
;; dla pierwiastka 8-st --> trzykrotne tłumienie pozwala uzyskać przybliżoną wartość 

(define (eighth-root x)
  (fix-point (average-damp (average-damp (average-damp (lambda (y) (/ x (expt y 7)))))) 1.0))

;;(eighth-root 254) ≈ 2

;; dla pierwiastka 16-st --> czterokrotne tłumienie
(define (sixteenth-root x) (fix-point((repeated average-damp 4) (lambda (y) (/ x (expt y 15)))) 1.0))

;;(sixteenth-root 65536) ≈ 2
;; stąd wniosek, że aby uzyskać pierwiastek n-tego stopnia z liczby należy
;; złożyć funckję average damp (log n 2) razy 



;; obliczanie pierwiastka n-tego stopnia z liczby
(define (nth-root x n)
  (cond
    [(= n 1) 1]
    [else    (fix-point ((repeated average-damp (log n 2))
              (lambda (y) (/ x (expt y (- n 1)))))  1.0)]))
 


(nth-root 64 4)
(nth-root 1 16)
(nth-root 1023 1)
(nth-root 254 8)
(nth-root 4 2)
(nth-root -27 3)
(nth-root 1024 4)
(nth-root 3215 5)
(nth-root 11111111 6)