V=int(input())
P1=int(input())
P2=int(input())
H=float(input())
v_pipes=P1*H+P2*H
if v_pipes<=V:
    print(f"The pool is {v_pipes/V*100:.2f}% full."
          f" Pipe 1: {(P1*H)/v_pipes*100:.2f}%."
          f" Pipe 2: {(P2*H)/v_pipes*100:.2f}%.")
elif v_pipes>V:
    print(f"For {H} hours the pool overflows with"
          f" {(v_pipes-V):.2f} liters.")
