* Tree
* Segment Tree
* Fenwick Tree



가. Tree

1. Tree란?

   가) 노드 간 계층과 1:N 관계를 갖는 자료구조

   * <img width="629" alt="화면 캡처 2022-11-29 104550" src="https://user-images.githubusercontent.com/109324632/204418117-0c06d4a6-8a1f-422f-b56e-ee249dc097ff.png">

2. Tree - Degree(차수)

   가) 노드에 연결된 자식 노드의 개수

   * <img width="614" alt="화면 캡처 2022-11-29 104751" src="https://user-images.githubusercontent.com/109324632/204418326-27c957e6-5aa1-43d4-80bf-8a832338c6cb.png">

3. Tree - Level, Height, Depth(레벨, 높이, 깊이)

   가) 일반적으로 루트 노드부터 가장 높은 레벨을 말함

   * <img width="723" alt="화면 캡처 2022-11-29 105001" src="https://user-images.githubusercontent.com/109324632/204418604-7b732938-83ce-4742-bc2a-4a40b293d03a.png">

4. Binary Tree(이진 트리)란?

   가) 모든 노드가 최대 2개의 자식 노드를 가질 수 있는 트리

   * <img width="796" alt="화면 캡처 2022-11-29 105134" src="https://user-images.githubusercontent.com/109324632/204418810-99c568b2-9832-4b4c-88b9-ecdbc88b8b8c.png">

5. Binary Tree - 노드의 개수 구하기

   가) 특정 레벨에서의 최대 노드 개수

   * <img width="589" alt="화면 캡처 2022-11-29 105613" src="https://user-images.githubusercontent.com/109324632/204419467-1022997b-c74c-477c-a0e5-057e5f309469.png">

   나) 높이가 H일 때, Binary Tree가 가질 수 있는 노드의 수

   * <img width="845" alt="화면 캡처 2022-11-29 105736" src="https://user-images.githubusercontent.com/109324632/204419621-d98d4f67-eaa1-4f4d-a278-2849052283f1.png">

6. Binary Tree - Full Binary Tree (포화 이진 트리)

   가) 모든 노드가 2개의 노드를 가지고 있는 트리

   * ![화면 캡처 2022-11-29 110201](C:\Users\정유현\Desktop\화면 캡처 2022-11-29 110201.png)

7. Binary Tree - Complete Binary Tree (완전 이진 트리) - 힙 관련

   가) 높이가 H이고 노드의 개수가 N일 때, 빈 자리 없이 채워지는 트리

   * <img width="728" alt="화면 캡처 2022-11-29 110253" src="https://user-images.githubusercontent.com/109324632/204420322-2499cbcf-408f-45c8-b6c7-85838b63b6ce.png">

8. Binary Tree - Skewed Binary Tree (편향 이진 트리) - 별로 사용 안 함(리스트 사용하면 되니깐)

   가) 높이가 H일 때, 최소 노드 개수를 가지면서 한쪽 방향으로 노드는 가지는 트리

   * <img width="759" alt="화면 캡처 2022-11-29 110633" src="https://user-images.githubusercontent.com/109324632/204420800-5f73c3ef-8a23-4e02-aecf-bdebf087898d.png">

9. Binary Tree - Traversal (순회)

   가) Traversal (순회)란 트리의 각 노드를 중복되지 않게 전부 방문하는 것

   나) 비선형구조로 선형구조처럼 선후 연결 관계를 알 수 없다.

   다) 트리의 순회 방법

   * 전위 순회 : V(부모) -> L -> R
     * L = V*2
     * R = V*2+1
   * 중위 순회
   * 후위 순회

나. Segment Tree

1. 어떤 데이터가 존재할 때, 특정 구간의 결과값을 구하는데 사용하는 자료구조

   가) <img width="826" alt="화면 캡처 2022-11-29 113943" src="https://user-images.githubusercontent.com/109324632/204425323-66d4cd5c-d7e6-4a88-bb44-b93a9609f508.png">

   나) 

