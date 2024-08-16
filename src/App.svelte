<script>
  import Router from "svelte-spa-router";
  import Login from "./pages/Login.svelte";
  import Main from "./pages/Main.svelte";
  import Signup from "./pages/Signup.svelte";
  import Write from "./pages/Write.svelte";
  import NotFound from "./pages/NotFound.svelte";
  import "./css/style.css";
  import { user$ } from "./store";
  import {
    getAuth,
    GoogleAuthProvider,
    signInWithCredential,
  } from "firebase/auth";
  import { onMount } from "svelte";
  import Loading from "./pages/Loading.svelte";
  import MyPage from "./pages/MyPage.svelte";

  let isLoading = true;

  const auth = getAuth();

  const checkLogin = async () => {
    const token = localStorage.getItem("token");
    if (!token) return (isLoading = false);

    const credential = GoogleAuthProvider.credential(null, token);
    const result = await signInWithCredential(auth, credential);
    const user = result.user; //유저 정보 가져오기
    user$.set(user); // 유저 정보 업데이트
    isLoading = false;
  };

  const routes = {
    "/": Main,
    "/signup": Signup,
    "/write": Write,
    "/My": MyPage,
    "*": NotFound,
  };

  onMount(() => checkLogin());
</script>

{#if isLoading}
  <Loading />
  <!--조건문을 사용해 로그인 페이지로 이동-->
{:else if !$user$}<!--유저 정보가 없으면 -->
  <Login /><!-- 로그인화면을 보여준다 -->
{:else}
  <!--있을때는-->
  <Router {routes} />
  <!--라우터 하던 화면을 보여주세요 ->12번 라인-->
{/if}
