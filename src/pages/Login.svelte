<script>
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";

  const provider = new GoogleAuthProvider();
  const auth = getAuth();

  const loginWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
      const user = result.user;
      user$.set(user);
      localStorage.setItem("token", token);
    } catch (error) {
      console.error(error); //error 발생시 error 표시
    }
  };
</script>

<div>
  {#if $user$}
    <div>{$user$?.displayName}</div>
  {/if}

  <!--로그인 정보 업데이트-->
  <div>로그인하기</div>
  <button class="login-btn" on:click={loginWithGoogle}>
    <img
      class="google-img"
      src="https://w7.pngwing.com/pngs/869/485/png-transparent-google-logo-computer-icons-google-text-logo-google-logo-thumbnail.png"
      alt=""
    />
    <!--src로 특정 링크 넣어서 이미지 가져오기-->
    <div>Google로 시작하기</div>
    <div />
  </button>
</div>

<style>
  .login-btn {
    width: 200px;
    height: 50px;
    border: 1px solid gray;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    border-radius: 3px;
  }

  .google-img {
    width: 20px;
  }
</style>
