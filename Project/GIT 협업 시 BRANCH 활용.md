#### GIT 협업 시 BRANCH 활용

```bash
git branch 'branch 이름' : 브랜치 만들기
git switch 'branch 이름' or git checkout 'branch 이름' : 브랜치 들어가기
git status : 상태 확인
git add .
git commit -m ''
git push origin master

올리고 나서 병합 후
git checkout master : master로 가기
git branch -D 'branch 이름' : 브랜치 삭제하기(로컬에서 삭제)

다른 사람이 변경한게 있으면 풀 받기
git pull origin master

git branch 'branch 이름'
git checkout 'branch 이름' : 브랜치 들어가기
touch README.md : 파일 만들기(변경이 있으면)
git add .
git commit -m ''
git push origin master

git checkout master : master로 가기
git branch -D 'branch 이름' : 브랜치 삭제하기(로컬에서 삭제)

vscode 세번째탭에서 확인 가능
```

