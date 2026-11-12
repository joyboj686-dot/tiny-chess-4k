import json,os,urllib.request as U
N=[33,31,18,14,-33,-31,-18,-14]
K=[1,-1,16,-16,15,-15,17,-17]
V=[0,100,320,330,500,900,0]
Z=lambda r:[(ord(c)-104)*5 for c in r]
PM=[0,*map(Z,"hhijkmph dhijkkif fiijjihg hhhhijki ghhhhhhh jhfdb```".split())]
X=Exception
def att(b,s,c):
 for d in N:
  t=s+d
  if not t&136 and b[t]==2+c:return 1
 for d in(15,17):
  t=s+(d if c else-d)
  if not t&136 and b[t]==1+c:return 1
 for i,d in enumerate(K):
  t=s+d
  while not t&136:
   p=b[t]
   if p:
    if p&8==c and(p&7 in(5,4-(i>3))or p&7==6 and t==s+d):return 1
    break
   t+=d
def gen(b,w,cs,ep,q=0):
 o=8-8*w;e=8*w;m=[]
 def A(f,s,l):
  if b[f]&7==1 and s>>4==7*w:
   for r in(5,4,3,2):m.append(f|s<<7|r<<14|l<<17)
  else:m.append(f|s<<7|l<<17)
 for f in range(128):
  p=b[f]
  if f&136 or not p or p&8!=o:continue
  t=p&7
  if t==1:
   u=32*w-16
   for d in(u-1,u+1):
    s=f+d
    if s&136:continue
    if b[s] and b[s]&8==e:A(f,s,1)
    elif s==ep:A(f,s,2)
   s=f+u
   if not b[s]:
    if not q or s>>4==7*w:A(f,s,0)
    if not q and f>>4==6-5*w and not b[s+u]:A(f,s+u,4)
   continue
  if t==6 and not q:
   c=cs>>2*(1-w)&3
   if c and not ck(b,w):
    if c&1 and not b[f+1]|b[f+2]and not att(b,f+1,e):A(f,f+2,8)
    if c&2 and not b[f-3]|b[f-2]|b[f-1]and not att(b,f-1,e):A(f,f-2,8)
  for d in(N if t==2 else K if t==6 else (K[4:],K[:4],K)[t-3]):
   s=f+d
   while not s&136:
    if b[s]:
     if b[s]&8!=o:A(f,s,1)
     break
    if not q:A(f,s,0)
    if t in(2,6):break
    s+=d
 return m
def mk(b,cs,ep,m):
 f=m&127;s=m>>7&127;pr=m>>14&7;l=m>>17
 b=b[:];p=b[f];b[s]=pr|p&8 if pr else p;b[f]=0;n=-1
 if l&2:b[s-16 if p<8 else s+16]=0
 if l&4:n=(f+s)//2
 if l&8:b[f+3 if s>f else f-4]=0;b[f+1 if s>f else f-1]=p&8|4
 if p&7==6:cs&=~(3<<2*(p>8))
 for q in(f,s):cs&=~R.get(q,0)
 return b,cs,n
ck=lambda b,w:att(b,b.index(14-8*w),8*w)
def legal(b,w,cs,ep,q=0):return[(m,c)for m in gen(b,w,cs,ep,q)for c in[mk(b,cs,ep,m)]if not ck(c[0],w)]
def ev(b,w):
 a=0
 for f in range(128):
  p=b[f]
  if f&136 or not p:continue
  t=p&7;c=p>>3;r=f>>4 if c==0 else 7-(f>>4);z=1-2*c
  a+=z*(V[t]+PM[t][r])
 return a if w else-a
R={0:2,7:1,112:8,119:4}
T={};KL={};n=0
def s(b,w,cs,ep,d,a,z,pl):
 global n
 n+=1
 if n>2e4:raise X
 chk=ck(b,w);q=d<=0;h=0;best=-9**5
 if q and not chk:
  best=ev(b,w)
  if best>=z:return best
  a=max(a,best)
 k=(bytes(b),w,cs,ep);e=T.get(k)
 if e and not q:
  h=e[3]
  if e[0]>=d and(e[2]<1 or e[1]>=z if e[2]<2 else e[1]<=a):return e[1]
 def key(x):
  m=x[0]
  if m==h:return 9**9
  if m>>17&3:return 9**7+V[b[m&127]&7]*10
  if m in KL.get(pl,()):return 9**5
  return 0
 ms=sorted(legal(b,w,cs,ep,q and not chk),key=key,reverse=True)
 if not ms:return(-30000+pl if chk else best if q else 0)
 bm=0;fl=2
 for m,c in ms:
  v=-s(c[0],not w,c[1],c[2],d-1,-z,-a,pl+1)
  if v>best:best=v;bm=m
  if v>a:a=v;fl=0
  if a>=z:
   fl=1
   if not q and not m>>17&1:
    KL[pl]=[m]+KL.get(pl,[])[:1]
   break
 if not q:T[k]=(d,best,fl,bm)
 return best
def uci(m):
 r=lambda x:chr(97+(x&7))+str((x>>4)+1)
 p=m>>14&7
 return r(m&127)+r(m>>7&127)+" pnbrq"[p].strip()
def best(b,w,cs,ep,L):
 global n
 n=0;T.clear();KL.clear()
 ms=[m for m,c in legal(b,w,cs,ep)if uci(m)in L]
 bm=ms[0]
 try:
  for d in range(1,8):
   a=-9**5;cb=bm
   for m in[bm]+[x for x in ms if x!=bm]:
    c=mk(b,cs,ep,m)
    v=-s(c[0],not w,c[1],c[2],d-1,-9**5,-a,1)
    if v>a:a=v;cb=m
   bm=cb
 except X:pass
 return uci(bm)
def fen(F):
 p,c,r,e,*_=F.split();b=[0]*128;cs=sum(1<<i for i,x in enumerate("KQkq")if x in r)
 for i,r in enumerate(p.split("/")):
  x=0
  for ch in r:
   if ch.isdigit():x+=int(ch)
   else:b[(7-i)*16+x]="xPNBRQK".index(ch.upper())+8*ch.islower();x+=1
 return b,c=="w",cs,-1 if e=="-"else ord(e[0])-97+16*(int(e[1])-1)
def P(p,x):
 return json.load(U.urlopen(U.Request(E+p,json.dumps(x).encode(),{"content-type":"application/json"})))
if __name__=="__main__":
 E=os.environ["MAKEFUN_ENV_URL"]
 while 1:
  g=P("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   L=g["legal_moves"]
   try:m=best(*fen(g["fen"]),L)
   except:m=L[0]
   g=P("/move",{"game":g["game"],"move":m})