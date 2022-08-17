#### STACK

* 스택
* 재귀호출
* Memoization
* DP
* DFS



가. 스택

1. 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조(자료구조란 저장하는 것)

2. 스택에 저장된 자료는 선형 구조(한 줄로 쭉 늘어놨다.)

   가) 선형구조 : 자료 간의 관계가 1대1의 관계

   나) 비선형구조 : 자료 간의 관계가 1대N의 관계를 갖는다.(예:트리)

3. 스택에 자료 삽입 혹은 자료 꺼낼 수 있다.

4. 마지막에 삽입합 자료를 가장 먼저 꺼낸다. 후입선출(LIFO, Last-In-First-Out)

   가) 스택에 1,2,3 순으로 자료를 삽입한 후 꺼내면 역순으로 즉 3,2,1 순으로 꺼낼 수 있다.

나. 스택의 구현

1. 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산

   가) 자료구조 : 자료를 선형으로 저장할 저장소

     1)배열을 사용할 수 있다.

     2)저장소 자체를 스택이라 부르기도 한다.

     3)스택에서 마지막 삽입된 원소의 위치를 top(stack pointer, sp)이라 부른다

   나) 연산

     1)삽입 : 저장소에 자료를 저장한다. 보통 push라고 부른다.

     2)삭제 : 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 pop이라고 부른다.

     3)스택이 공백인지 아닌지를 확인하는 연산 : isEmpty / 비어있는 스택에 pop을 날리면 안되니 비어있는지 확인. 비어있으면 True, 비어있지 않으면 False

     4)스택의 top에 있는 item(원소)을 반환하는 연산 : peek

   ```
   * 스택의 삽입/삭제 과정
   4
   3
   2
   1
   0 
   공백스택 top은 -1에 있음
   
   (push는 1. top을 증가시킴, 2. stack[top]에 A를 저장해)
   
   push A 하면
   4
   3
   2
   1
   0 A top
   
   push B 하면
   4
   3
   2
   1 B top
   0 A
   
   push C 하면
   4
   3
   2 C top
   1 B
   0 A
   
   pop C 하면
   4
   3
   2 C 
   1 B top
   0 A
   ```

2. 스택의 push 알고리즘

   ```python
   # append 메소드를 통해 리스트의 마지막에 데이터 삽입 => append pop 느려!!
   def push(item):
   	s.append(item)
   
   
   def push(item, size):
   	global top
   	top += 1
   	if top==size:
   		print('ovefflow!') # 디버깅용
   	else:
   		stack[top] = item
   
   size = 10 # 리스트보다 빨라
   stack = [0]*size
   top = -1
   
   # push(20) 이렇게 풀어서 구현 가능!!
   top += 1
   stack[top] = 20
   ```

3. 스택의 pop 알고리즘

   ```python
   def pop():
   	if len(s) == 0:
   		# underflow
   		return
   	else:
   		return s.pop(-1);
   
   
   def pop():
   	global top
   	if top == -1:
   		print('underflow')
   		return 0
   	else:
   		top -= 1 # top을 감소시키고
   		return stack[top+1] # 내려놓기 전의 값을 리턴해줘
   		# 따로 지우지 않아도 돼, 어차피 push되면 다른 값으로 덮어써지기 때문
   print(pop())
   
   if top > -1: # pop()
   	top -= 1
   	print(stack[top+1])
   
   # 혹은
   data = stack[top]
   top -= 1
   ```

   ```python
   # 스택 구현
   # 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력
   
   stackSize = 10
   stack = [0] * stackSize
   top = -1
   
   top += 1 # push(1)
   stack[top] = 1
   
   top += 1 # push(2)
   stack[top] = 2 
   
   top += 1 # push(3)
   stack[top] = 3
   
   data = stack[top]
   top -= 1
   print(data)
   
   data = stack[top]
   top -= 1
   print(data)
   
   top -= 1 
   data = stack[top+1]
   print(data)
   
   
   # append, pop 이용
   stack2 = []
   stack2.append(10)
   stack2.append(20)
   print(stack2.pop()) # 20
   print(stack2.pop()) # 10
   
   # 문제에서는 크기 예측 가능, 1차원 배열 사용하면 됨
   # 동적으로 할당은 동적 연결리스트를 이용한다는 것, 스택 모자라면 늘린다라는 얘기, 우리는 다루진 않는다.
   ```

4. 스택의 응용1 : 괄호검사

   가) 괄호의 종류 : 대 중 소

   나) 조건

     1)왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.

     2)같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.

     3)괄호 사이에는 포함 관계만 존재 : 소 < 중 < 대

   다) 스택을 이용한 괄호 검사

   ```python
   ( 나오면 ( push
   ( 나오면 ( push
   ) 나오면 ( pop하여 비교
   
   정상적인 경우라면 stack에 아무것도 없어야 됨
   그러나 stack이 비어있는데 pop하라고 하면 그것도 안돼
   ```

5. 스택의 응용2 : function call

   가) 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리

     1)가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리

     2)함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입

     3)함수의 실행이 끝나면 시스템 스택의 top원소(스택 프레임)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀

     4)함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

다. 재귀호출

1. 자기 자신을 호출하여 순환 수행되는 것, 자기 자신에게 너무 얽매이지 말고 반복되는게 많으니깐 재귀로 만들어보자! 이런 느낌임..

2. 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성

   예) factorial (사실은 재귀 잘 안 씀)

   ```python
   # n에 대한 factorial : 1부터 n까지의 모든 자연수를 곱하여 구하는 연산
   n! = n * (n-1)!
   	(n-1)! = (n-1) * (n-2)!
   	.
   	.
   	.
   
   def f(n):
   	if n == 1
   		return 1
   	else:
   		return n * f(n-1) # 반복문이 아니고..
   
   # 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복
   ```

   예) 피보나치 : 이전의 두 수 합을 다음 항으로 하는 수열 (이전의 두 수 합은 정의해줘야 함.)

   ```python
   def f(n):
   if n < 2:
   	return n
   else:
   	return f(n-1) + f(n-2)
   
   
   # 재귀호출은 두개의 인덱스를 갖는게 기본
   f(i, N) # i는 현재 단계, N은 목표
   f(0, 3) # 0단계, 목표3
   
   
                 f(0, 3)           f(i, N)
   ------------------------          if i == N # 목표에 도달
   i = 0         f(i, N)               return
   N = 3                             else:
   			  f(i+1, N)             f(i+1, N) # 다음단계로
   -------------------------
   i = 1         f(i, N)
   N = 3  
   			  f(i+1, N)
   -------------------------
   i = 2         f(i, N)
   N = 3  
   			  f(i+1, N)
   -------------------------
   i = 3         f(i, N)
   N = 3 
                 if i == N # 목표에 도달
   				return
   
   
   def f(i, N): # i 현재 단계, N 목표 단계
   	if i == N:
   		# 목표치에서 할 일
   		return
   	else:
   		# 재귀호출 전에 단계별로 할 일, 여기서 많이 씀
   		f(i+1, N)
   		# 재귀호출 이후에도 여기에 쓸 수 있음.
   
   f(0, 3)
   
   
   # 크기가 N인 배열의 모든 원소에 접근하는 재귀함수(많음!)
   def f(i, N): 
   	if i == N:    # 배열을 벗어남
   		return
   	else:         # 남은 원소가 있는 경우
   		B[i] = A[i]
   		f(i+1, N)   # 다음 원소로 이동
   
   N = 3
   A = [1, 2, 3]
   B = [0]*N
   f(0, N) # 0번 원소부터 N개의 원소에 접근
   # N이 1000이면 초과했다고 나옴(생각보다 깊진 않음, 15번정도..)
   ```

라. Memoization

1. 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은 ‘엄청난 중복 호출이 존재한다’라는 문제점이 있다. O(n^2)

2. 메모이제이션은 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술 ⇒ 동적 계획법의 핵심이 되는 기술

3. 메모이제이션은 ‘메모리에 넣기’라는 의미

   ```python
   def fibo1(n):
   	if n >= 2 and len(memo) <= n:
   		memo.append(fibo1(n-1)+fibo(n-2))
   	return memo[n]
   
   memo = [0, 1]
   ```

   ```python
   # 팩토리얼
   def f(n):
   	if n <= 1:
   		return 1
   	else:
   		return n * f(n-1)
   
   for i in range(21):
   	print(f(i))
   
   # 피보나치
   def fibo(n):
   	if n <= 1:
   		return n
   	else:
   		return fibo(n-1) + fibo(n-2)
   
   for i in range(21):
   	print(fibo(i))
   
   # 메모이제이션
   def fibo(n):
   	if n >= 2 and memo[n] == 0: # if memo[n] == -1:
   		memo[n] = fibo(n-1) + fibo(n-2)
   	return memo[n]
   
   memo = [0] * 101 # memo = [-1] * 101
   memo[0] = 1
   memo[1] = 1
   
   for i range(101):
   	print(fibo(i))
   ```

마. DP(Dynamic Programming)

1. 동적 계획 알고리즘은 그리디 알고리즘과 같이 “최적화 문제”를 해결하는 알고리즘이다.

2. 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.

3. 피보나치 수 DP 적용

   가) 메모이제이션은 뒤에서 앞으로 오는 거라면.. DP는 앞에서 뒤로

   나) DP는 테이블이 나옴, 테이블을 채워나가보면

   ```python
   def fibo2(n):
   	f = [0, 1]
   
   	for i in range(2, n+1):
   		f.append(f[i-1] + f[i-2])
   
   	return f[n]
   
   
   def fibo_dp(n):
   	table[0] = 0
   	table[1] = 1
   	for i in range(2, n+1):
   		table[i] = table[i-1] + table[i-2]
   	return 
   
   table = [0]*101
   fibo_dp(100)
   
   
   # 테스트케이스가 많으면 미리 구해놓고 가져다 출력
   T = int(input())
   for tc in range(1, T+1):
   	N = int(input()
   	print('#{} {}'. format(tc, table[N]))
   
   # 마지막 값만 구한다면 필요한 변수 두 개만 가지고..
   a, b = b, a+b
   
   a = 0
   b = 1
   n = 20
   for _ in range(n-1): # n = 2라면 1번만 계산하면 되니
   	a, b = b, a+b
   print(b)
   ```

4. 메모이제이션을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다.

바. DFS(깊이우선탐색)

1. 비선형구조(1:n은 트리, n:n은 그래프)인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

2. 두 가지 방법

   가) 깊이 우선 탐색(Depth First Search, DFS)

   나) 너비 우선 탐색(Breadth First Search, BFS)

3. 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

4. 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택(저장하는 방법, 재귀호출 이용해서도 저장할 수 있음) 사용

5. 알고리즘

   가) 시작 정점 v를 결정하여 방문한다.

   나) 정점 v에 인접한 정점 중에서

     1)방문하지 않은 정점 w가 있으면, 정점 v를 스택에 “push”하고 정점 w를 방문한다. 그리고 “w를 v로 하여” 다시 나)를 반복한다.

     2)방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 “pop”하여 받은 “가장 마지막 방문 정점을 v로 하여” 다시 나)를 반복한다.

   다) 스택이 공백이 될 때까지 나)를 반복한다.

   ```python
   visited[], stack[] 초기화 # 방문한 곳, 
   DFS(v)
   	시작점 v 방문;
   	visited[v] <- true
   	while {
   				if (v의 "인접 정점" 중 방문 안 한 정점 w가 있으면)
   					push(v)
   					v <- w
   					visited[w] <- true
   				else
   					if (스택이 비어 있지 않으면)
   						v <- pop(stack)
   					else
   						break
   	}
   end DFS()
   ```

   ```python
   초기상태 : 배열 visited를 False(혹은 0)로 초기화하고, 공백 스택을 생성
   
   A 방문
   visited[A] <- true
   
   방문하지 않은 인접인 정점을 간다. (B방문)
   push(A)
   V <- W
   visited[B] <- true 
   
   (D방문)
   push(B)
   V <- W
   visited[D] <- true
   .
   .
   .
   (C방문)
   push(E)
   V <- W
   visited[C] <- true
   
   (되돌아감)
   v <- pop(stack)
   
   stack이 비면 종료
   ```

   ```python
   # A~G -> 0~6
   adjust = [[1, 2],    			 # 0
   		  [0, 3, 4], 			 # 1
   		  [0, 4],    			 # 2
             [1, 5],    			 # 3
             [1, 2, 5], 			 # 4
             [3, 4, 6], 			 # 5
   		  [5]]       			 # 6
   
   def dfs(v, N):
   	visited = [0] * N     		 # visited 생성
   	stack = [0] * N       		 # stack 생성
   	top = -1
   	print(v)               		 # 방문
   	visited[v] = 1         	 	 # 시작점 방문 표시
   	while True:
   		for w in adjust[v]: 	 # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
   			if visited[w] = 0:
   				top += 1         # push(v)
   				stack[top] = v
   				v = w            # v <- w (w에 방문)
   				print(v)         # 방문
   				visited[w] = 1   # visited[w] <- true
   				break
   		else:               	 # w가 없으면
   			if top != -1:		 # 스택이 비어 있지 않은 경우
   				v = stack[top]   # pop
   				top -= 1
   			else:              	 # 스택이 비어 있으면
   				break            # while 빠져나옴
   
   dfs(0, 7)
   ```

   ```python
   '''
   0번부터 V번까지, E개의 간선
   6 8
   0 1
   0 2
   1 3
   1 4
   2 4
   3 5
   4 5
   5 6
   '''
   V, E = map(int, input().split()) # 6 8
   N = V + 1
   adjust = [[] for _ in range(N)]
   for _ in range(E):
   	s, e = map(int, input().split())
   	adjust[s].append(e)
   	adjust[e].append(s) # 반대도 줘야함
   ```

   ```python
   def dfs(v):
   	print(v) # v 방문
   	visited[v] = 1
   	for w in adjust[v]:
   		if visited[w] == 0: # 방문하지 않은 w
   			dfs(w)
   
   V, E = map(int, input().split()) # 6 8
   N = V + 1
   adjust = [[] for _ in range(N)]
   for _ in range(E):
   	s, e = map(int, input().split())
   	adjust[s].append(e)
   	adjust[e].append(s) # 반대도 줘야함
   
   visited = [0]*N
   dfs(0)
   ```

   