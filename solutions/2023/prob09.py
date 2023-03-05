freq = int(input())
c = int(input())
vr = int(input())*1000/3600
vs = int(input())*1000/3600

res = freq*((c+vr)/(c+vs))
print(f"{res:.02f} Hz")