<h1> 프로젝트 개요 </h1>

**Inter Art(Interact ART)** 프로젝트는 Django를 사용하여 그림이나 사진 등을 서로 공유할 수 있는 게시판 입니다.

<br>
<br>

<h1> 프로젝트 기간 </h1>

- **v1.0** : 23/06/27 - 23/07/09

<br><br>

<h1> 사용 기술 </h1>

- Python
- Django
- MySQL
- HTML
- Javascript
- CSS

<br><br>

<h1> 데이터베이스 </h1>

- User Table : 회원가입 한 유저 정보 저장
  - id : pk

  - username : 가입 아이디
  - password : 단방향 암호화된 비밀번호
  - last_login : 마지막 로그인 날짜
  - is_superuser : 슈퍼계정 확인
  - first_name : 이름
  - last_name : 성
  - email : 가입 이메일
  - gender : 성별

<br>

- Post Table : 게시물 정보 저장
  - id : pk

  - title : 제목
  - content : 내용
  - image : 이미지 파일 저장 결로
  - created_at : 게시물 생성 날짜
  - updated_at : 게시물 수정 날짜
  - like_user : 좋아요 기능을 위한 User Table과의 Many to Many 관계 컬럼
  - coment_user : 게시물에 댓글 단 유저 (fk)

<br>

- Comment Table : 댓글 정보 저장
  - id : pk

  - comment : 내용
  - created_at : 댓글 생성 날짜
  - updated_at : 댓글 수정 날짜
  - post_id : Post Table (fk)
  - user_id : User Table (fk)

<br>

- Notice Table : 공지사항 정보 저장

  - id : pk

  - title : 제목
  - content : 내용
  - image : 이미지 파일 경로
  - created_at : 공지사항 생성 날짜

<br><br>

<h1>프로젝트 기능</h1>

- 회원가입 구현
  - 아이디, 비밀번호, 이름, 성별, 이메일 정보를 통한 회원가입

  - Django form을 이용하여 데이터 유효성 검사
  - 중복 email로 회원가입 불가
  - 비밀번호 단방향 암호화 후 저장
  - 회원가입 완료 후 로그인 페이지로 redirect

<br>

- 로그인 구현
  - User DB에 저장된 정보를 기반으로 로그인 여부 구현

  - 세션 타임아웃 (20분) 설정

<br>

- 메인 홈
  - Django의 Admin 기능을 활용하여 공지사항 게시글 관리 기능

  - 일주일 동안 가장 많은 좋아요를 받은 게시물 게시

<br>

- 게시판
  - 페이징 기능 추가

  - 검색 기능 추가 (게시물 내용, 게시물 작성자, 댓글 내용, 댓글 작성자 기반)
  - 글쓰기 기능 추가
  - 댓글 수 보여주기 기능 추가

<br>

- 디테일 페이지
  - 좋아요 기능 추가

  - 댓글 기능 추가
  - 게시물 작성자와 로그인 정보 기반으로 게시물 수정 및 삭제 기능 추가
  - 댓글 작성자와 로그인 정보 기반으로 댓글 수정 및 삭제 기능 추가

<br>

- 내 게시물 관리 페이지 추가

**TODO**

- 그림그리기 개발

<br><br>

<h1> 프로젝트 디자인 </h1>

<h2>v1.0</h2>

<h3>로그인</h3>

<img src="./imgs/%EB%A1%9C%EA%B7%B8%EC%9D%B8.png">

<br><br>

<h3>회원가입</h3>

<img src="./imgs/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.png">

<br><br>

<h3>로그인 및 회원가입 데이터 유효성</h3>

<img src="./imgs/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%9C%A0%ED%9A%A8%EC%84%B1.png">

<br><br>

<h3>메인</h3>

<img src="./imgs/%EB%A9%94%EC%9D%B8%20%ED%99%88.png">

- 공지사항 : 운영자(슈퍼계정)가 작성한 공지사항

- 주간 Top 10 : 일주일 동안 가장 많은 좋아요를 받은 게시물

<br><br>

<h3>공지사항</h3>

<img src="./imgs/%EA%B3%B5%EC%A7%80%EC%8B%9C%ED%95%AD.png">

- Django의 admin기능을 통해 공지글 작성 및 관리 가능

<br><br>

<h3>게시판</h3>

<img src="./imgs/%EA%B2%8C%EC%8B%9C%ED%8C%90.png">

 - 게시물 정보 및 댓글 수 보여주기(초록색 텍스트)

<br><br>

<h3>게시글 검색</h3>

<img src="./imgs/%EA%B2%8C%EC%8B%9C%ED%8C%90%20%EA%B2%80%EC%83%89.png">

- 검색 폼에 입력한 키워드를 기반으로 **게시글 내용, 게시글 작성자, 댓글 내용, 댓글 작성자** 검색

<br><br>

<h3>게시글 작성</h3>

<img src="./imgs/%EA%B2%8C%EC%8B%9C%EA%B8%80%20%EC%9E%91%EC%84%B1.png">

<br><br>

<h3>디테일 페이지</h3>

<img src="./imgs/%EB%94%94%ED%85%8C%EC%9D%BC%20%ED%8E%98%EC%9D%B4%EC%A7%80.png">
<img src="./imgs/%EC%A2%8B%EC%95%84%EC%9A%94%20%EB%B0%8F%20%EB%8C%93%EA%B8%80.png">

<br><br>

<h3>게시글 수정 및 삭제</h3>

<img src="./imgs/%EC%88%98%EC%A0%95%EA%B0%80%EB%8A%A5.png">
<img src="./imgs/%EC%88%98%EC%A0%95%EB%B6%88%EA%B0%80.png">

- 로그인 정보를 기준으로 게시물 수정 및 삭제 권한 확인

<br><br>

<h3>좋아요 및 댓글</h3>

<img src="./imgs/%EC%A2%8B%EC%95%84%EC%9A%94%20%EB%B0%8F%20%EB%8C%93%EA%B8%80%20%EA%B8%B0%EB%8A%A5.png">

- 계정당 1회 좋아요 기능

<br><br>

<h3>댓글 수정 및 삭제</h3>

<img src="./imgs/%EB%8C%93%EA%B8%80%20%EC%88%98%EC%A0%95%20%EC%82%AD%EC%A0%9C.png">

- 댓글 작성자와 로그인 정보를 기반으로 댓글 수정 및 삭제 권한 확인

<br><br>

<h3>내 게시물 관리</h3>

<img src="./imgs/%EB%82%B4%20%EA%B2%8C%EC%8B%9C%EB%AC%BC%20%EA%B4%80%EB%A6%AC.png">

- 내가 작성한 게시글 관리 페이지
