<form id="signup-form" action="/signup" method="POST">
  <!-- action어디 주소로 보낼건지?->/signup -->
  <div>회원 가입</div>
  <div>
    <label for="id">아이디</label>
    <input type="text" id="id" name="id" required />
  </div>
  <div>
    <label for="password">패스워드</label>
    <input
      type="password"
      id="password"
      name="password"
      autocomplete="on"
      required
    />
  </div>
  <div>
    <label for="password2">패스워드 확인</label>
    <input
      type="password"
      id="password2"
      name="password2"
      autocomplete="on"
      required
    />
  </div>
  <div>
    <label for="name">이름</label>
    <input type="text" id="name" name="name" required />
  </div>
  <div>
    <label for="email">이메일</label>
    <input type="email" id="email" name="email" required />
  </div>
  <div>
    <button type="submit">회원 가입하기</button>
  </div>
  <div id="info"></div>
</form>
