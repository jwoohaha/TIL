# 1/12 TIL

## GIT

> git은?

    리누스 토발즈가 만든 버전관리 프로그램

> github란?

    git을 원격으로 저장할 수 있는 클라우드 저장소 < - > 로컬 레포지토리

    보관 및 공유에 용이함

- Working Directory / Staging Area / Repository로 나뉨
  
  1.Working Dir: 작업하고 있는 실제 디렉토리
  
  2.Staging Area: 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
  
  3.Repository: 커밋들이 저장되는 곳
  
  Staging Area의 존재 이유: 원하는 것들만 커밋하여 버전으로 남기기 위해
  

- `git init` : git local repo 초기화 (root 폴더에서는 하면 안됨)
  
  1. 단 한번이라도 `git add` staging area로 옮겨줘야 함
    
  2. 파일의 상태
    
    1. 최초 생성 시: untracked
      
    2. git add 후: staged
      
    3. git commit: tracked
      
    4. 파일의 수정이 있을 때: modified
      
    5. 최신이면: up-to-date
      
- `git add`: Working Directory 에서 Staging Area로
  
  1.`git add` . : 해당 디렉토리 모두
  
  2.`git add {file name}` : file을 지정해서 stage
  
- `git commit -m '커밋 메시지'`: Repository로
  
- `git status`: git 상태 알려줌
  
- `git log`: commit 히스토리 보여줌 (옵션: --oneline, graph)
  

여기까지가 Local Repository에서 일어나는 일들

---

## Remote Repository (깃허브)

- `git remote add origin {repo_Url}` 레포지토리 연결
  
- `git remote -v` : 확인
  
- `git push -u origin master` (-u 옵션 다음부터는 git push로 가능)
  

- add -> commit -> push
  
- 원격으로 만든 후 git clone
  

---

## Linux

- tab : 자동완성
  
- mkdir : 디렉토리 생성
  
- touch : 파일생성
  
- ls : 내부 보여줌
  
- rm : 삭제
  
- cd ~ : root directory (절대경로)
  
- ./ : 현재 위치 (상대경로)
  
- ../ : 부모 디렉토리
  
- find -name 777 : 777이라는이름을 가진 폴더 혹은 파일 찾기
  

---

## MARKDOWN

- 제목 (#)
  
  - 글자 크기를 위해 제목 태그(#) 를 사용하면 안됨
    
  - 문서 구조를 잡아주는 역할
    
- 리스트 (* or -)
  
- 코드블럭 (백틱)
  
  문장을 작성하다가 ` 사용
  

```
print(test)
```

3개 사용 시 multiline

```
print(test)
print(test)
print(test)
```

- 이미지 ![string](img_url
  
  이미지 너비는 조정 불가 (html로 가능)
  
- 글자효과
  
  - 볼드처리 (별표 두개) **볼드**
    
  - 이탤릭 (별표 하나) *이탤릭*
    
  - 취소선 (물결 두개) ~~취소선~~
    
  - (—) 수평선 단락 구분
    
- 인용문(>)
  
  > hi there
