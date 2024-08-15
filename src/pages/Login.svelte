<form id="login-form" action="/signup" method="POST">
  <!-- action어디 주소로 보낼건지?->/signup -->
  <div>로그인하기</div>
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
    <button type="submit">로그인</button>
  </div>
  <div id="info"></div>
</form>
