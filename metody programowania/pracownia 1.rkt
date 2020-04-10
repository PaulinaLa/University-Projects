#lang racket
;; procedury pomocnicze 
(define (dist x y)
  (abs (- x y)))

(define (square x)
  (* x x))

(define (cube x) (* x x x))


;; główna procedura obliczająca pierwiastek 3-ciego stopnia
(define (cube-root x)
  ;; cond-for-better-one umożliwia generowanie kolejnych przybliżeń
  (define (cond-for-better-one x y)
    (/ (+ (/ x (* y y)) (* 2 y)) 3))
  ;; improve umożliwia poprawę przybliżenia
  (define (improve y)
    (cond-for-better-one x y ))
  (define (good-enough? y)
    (< (dist x (cube y)) 0.0001))
  (define (iter y)
    (cond
      [(good-enough? y) y]
      [ else            (iter (improve y))]))
  (iter 1.0))

;;testy
(cube-root 1) 
(cube-root 0) 
(cube-root 27)
(cube-root 8) 
(cube-root 64) 
(cube-root -1)
(cube-root -8)
(cube-root -27)
(cube-root 100000000000000)
(cube-root 12245678901234567)

