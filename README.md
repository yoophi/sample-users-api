# sample-users-api

Clean Architecture 기반의 Flask API Sample

## 도메인 로직

### Use Cases

- 유저를 신규 생성할 수 있다. `create`
- 유저를 조회할 수 있다. `get_list`
    - 조건에 맞는 유저를 조회할 수 있다.
    - 고유 id 를 이용해 유저를 조회할 수 있다.
- email 과 비밀번호로 유저를 인증할 수 있다. `authenticate`

### 제약 조건

- email, 비밀번호를 가진다.
- 유저의 email 은 고유하다. (-> repository)
- 유저의 id 는 고유하다. (-> repository)
