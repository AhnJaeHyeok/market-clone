<script>
  import { onMount } from "svelte";
  import Footer from "../components/Footer.svelte";
  import { getDatabase, ref, onValue } from "firebase/database";

  //여기 위에 있는 자바스크립트 파일은
  // 이 화면이 처음 렌더링 될때 처음 뜰 떄 한번만 뜨게 된다(한번실행)
  //그리고 나서 데이터를 가져오지 않음
  //화면이 보일때마다 실행되게 하고싶으면 onMount를 쓰면된다
  let hour = new Date().getHours();
  let min = new Date().getMinutes();

  $: items = []; // 5.이 문법을 사용할시 svelte가 알아서 업데이트
  //let 을 써도 값 자체가 바뀌기 때문에 let도 가능
  const calcTime = (timestamp) => {
    //한국시간 UTC +9시간
    const curTime = new Date().getTime() - 9 * 60 * 60 * 1000;
    const time = new Date(curTime - timestamp);
    const hour = time.getHours();
    const minute = time.getMinutes();
    const second = time.getSeconds();

    if (hour > 0) return `${hour}시간 전`;
    else if (minute > 0) return `${minute}분 전`;
    else if (second >= 0) return `${second}초 전`;
    else return "방금 전";
  };

  const db = getDatabase();
  const itemsRef = ref(db, "items/"); //1.이 값이 바뀔때마다
  onMount(() => {
    //onMount 추가 왜? 글쓰기 갔다오면 이미지 사라짐 현상때문에
    onValue(itemsRef, (snapshot) => {
      //2.스냅샷이 새롭게 내려온다
      const data = snapshot.val(); //3.바뀐 스냅샷은 이거야 너 화면 업데이트해
      items = Object.values(data).reverse(); // 4.이 데이터를 가지고 items를 업데이트 하고
    });
  });
</script>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <img src="assets/chart-bar.svg" alt="char-bar" />
      <img src="assets/wifi.svg" alt="wifi" />
      <img src="assets/battery.svg" alt="battery" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <div>역삼1동</div>
      <div class="menu-bar__location-icon">
        <img src="assets/arrow-down.svg" alt="" />
      </div>
    </div>
    <div class="menu-bar__icons">
      <img src="assets/serch.svg" alt="" />
      <img src="assets/menu.svg" alt="" />
      <img src="assets/alert.svg" alt="" />
      <div class="menu-bar__bell">1</div>
    </div>
  </div>
</header>

<main>
  {#each items as item}
    <div class="item-list">
      <div class="item-list__img">
        <img alt={item.title} src={item.imgUrl} />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">{item.title}</div>
        <div class="item-list__info-meta">
          {item.place}
          {calcTime(item.insertAt)}
        </div>
        <div class="item-list__info-price">{item.price}</div>
        <div>{item.description}</div>
      </div>
    </div>
  {/each}
  <a class="write-btn" href="#/write">+ 글쓰기</a>
</main>

<Footer location="home" />

<div class="media-info-msg">화면 사이즈를 줄여주세요.</div>
