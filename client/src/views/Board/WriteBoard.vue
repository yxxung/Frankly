<template>
  <body>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Out.svg" alt="나가기" />
      </a>
      <h2>글쓰기</h2>
      <div class="header--right">
        <!--제출 버튼-->
        <button class="write-button" type="submit" @click="onClickSubmit()">
          완료
        </button>
    <div class="wrap">
      <!--헤더-->
      <header class="header header--back">
        <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
          <img src="@/assets/icon/Out.svg" alt="나가기" />
        </a>
        <h2>글쓰기</h2>
        <div class="header--right">
          <!--제출 버튼-->
          <button
            v-if="writeFlag === 'write'"
            class="write-button"
            type="submit"
            @click="onClickSubmit()"
          >
            완료
          </button>
          <!--수정 제출 버튼-->
          <button
            v-else-if="writeFlag === 'update'"
            class="write-button"
            type="submit"
            @click="onClickUpdate()"
          >
            수정
          </button>
        </div>
      </header>

      <!--글쓰기 화면-->
      <div class="write-title">
        <!--카테고리-->
        <select v-model="regionName" class="region" @change="selected">
          <option v-for="region in regions" :key="region.value">
            {{ region.regionName }}
          </option>
        </select>

        <!--제목-->
        <input
          type="text"
          v-model="title"
          ref="title"
          class="board-title"
          placeholder="제목"
        />
      </div>

      <div class="write-content">
        <!--내용-->
        <textarea
          type="text"
          ref="content"
          v-model="content"
          class="board-content"
          placeholder="내용을 입력하세요."
          maxlength="2000"
        />
        <!--이미지 업로드 !!수정하기!!
          <label for="file">첨부파일</label>
          <input multiple @change="onInputImage()" id="file" ref="image" type="file" />-->
      </div>
    </header>

    <!--글쓰기 화면-->
    <div class="write-title">
      <!--카테고리-->
      <select v-model="regionName" class="region" @change="selected">
        <option
          v-for="region in regions"
          :key="region.value"
        >
          {{ region.regionName }}
        </option>
      </select>

      <!--제목-->
      <input
        type="text"
        v-model="title"
        ref="title"
        class="board-title"
        placeholder="제목"
      />
    </div>
    <div class="write-content">
      <!--내용-->
      <textarea
        type="text"
        ref="content"
        v-model="content"
        class="board-content"
        placeholder="내용을 입력하세요."
        maxlength="2000"
      />
      <!--이미지 업로드 !!수정하기!!
        <label for="file">첨부파일</label>
        <input multiple @change="onInputImage()" id="file" ref="image" type="file" />-->
    </div>
  </div>
  </body>
</template>

<script>
import axios from "axios";
export default {
  name: "WriteBoard",
  data() {
    return {
      regions: [
        { value: "0", regionName: "서울특별시" },
        { value: "1", regionName: "부산광역시" },
        { value: "2", regionName: "대구광역시" },
        { value: "3", regionName: "인천광역시" },
        { value: "4", regionName: "광주광역시" },
        { value: "5", regionName: "대전광역시" },
        { value: "6", regionName: "울산광역시" },
        { value: "7", regionName: "세종특별자치시" },
        { value: "8", regionName: "경기도" },
        { value: "9", regionName: "강원도" },
        { value: "10", regionName: "충청북도" },
        { value: "11", regionName: "충청남도" },
        { value: "12", regionName: "전라북도" },
        { value: "13", regionName: "전라남도" },
        { value: "14", regionName: "경상북도" },
        { value: "15", regionName: "경상남도" },
        { value: "16", regionName: "제주특별자치도" },
        { value: "17", regionName: "자유게시판" },
      ],
      title: "",
      content: "",
      image: "",
      writeFlag: "write",
    };
  },
  created() {
    const boardID = this.$route.params.boardID;
    if (boardID !== undefined) {
      this.writeFlag = "update"
      console.log(this.writeFlag);
      axios
        .get(`/api/boards/${boardID}`)
        .then((response) => {
          this.title = response.data.title;
          this.content = response.data.content;
          this.regionName = response.data.region;
        })
        .catch(() => {
          console.log("보드 내용을 불러오지 못했습니다.");
        });
    } else {
      this.writeFlag = "write"
      console.log(this.writeFlag);
    }
  },
  methods: {
    selected() {
      console.log(this.regionName);
    },
    /*onInputImage() {
      console.log(this.$refs);
      this.image = this.$refs.image.files[0];
    },*/
    onClickSubmit() {
      //입력된 내용이 없을 시
      if (this.title.length <= 0 || this.content.length <= 0) {
        window.alert("모든 내용을 입력해주세요!");
        return false;
      }
      /*
      const formdata = new FormData();
      this.image = this.$refs.image.files[0];
      formdata.append("region", this.region);
      formdata.append("region", this.regionName)
      formdata.append("title", this.title);
      formdata.append("content", this.content);
      formdata.append("image", this.image);*/
      axios
        .post("/api/boards/create", {
          title: this.title,
          region: this.regionName,
          content: this.content,
        })
        .then((response) => {
          // console.log(response);
          if (response.status === 200) {
            alert("게시글이 작성되었습니다.");
          }
          this.$router.go(-1);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onClickUpdate() {
      const boardID = this.$route.params.boardID;
      axios
        .put(`/api/boards/update/${boardID}`, {
          title: this.title,
          content: this.content,
          region: this.regionName,
        })
        .then((response) => {
          if (response.status === 200) {
            alert("게시글이 수정되었습니다.");
          }
          this.$router.go(-1);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
.write-button {
  margin: 0;
  background: black;
  width: 68px;
  height: 38px;
  font-family: "Noto Sans KR", sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  text-align: center;
  color: #ffffff;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
  0 2px 4px -1px rgba(0, 0, 0, 0.06);
  cursor: pointer;
  transition: 0.5s;
}
.header > h2 {
  margin: 0%;
  font-family: "Noto Sans KR", sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 22px;
  /* identical to box height */
  text-align: center;
  letter-spacing: -0.024em;
  color: #2b2b2b;
}
.write-title {
  padding-left: 10px;
  margin-top: 70px;
  display: flex;
}
/*카테고리*/
.region {
  width: 120px;
  height: 50px;
  padding: 0.8em 0.5em; /* 여백으로 높이 설정 */
  color: #a9a9a9;
  font-family: "Noto Sans KR", sans-serif;
  background: #fafafa;
  border-radius: 0px; /* iOS 둥근모서리 제거 */
}
/*제목*/
.board-title {
  margin-left: 10px;
  background: #fafafa;
  font-family: "Noto Sans KR", sans-serif;
  width: 410px;
  height: 50px;
  outline: none;
  padding-left: 10px;
}
.board-title::placeholder {
  color: #a9a9a9;
  font-size: 16px;
}
/*글쓰기*/
.write-content {
  margin-top: 10px;
  padding: 0 10px 0 10px;
}
.board-content {
  background: #fafafa;
  font-family: "Noto Sans KR", sans-serif;
  width: 530px;
  height: 350px;
  outline: none;
  resize: none;
  border: none;
  padding: 10px;
}
.board-content:focus {
  border: none;
}
.board-content::placeholder {
  color: #a9a9a9;
  font-size: 16px;
}
/*파일 첨부*/
.write-content label {
  display: inline-block;
  width: 100px;
  height: 45px;
  background-color: #4a4a4a;
  color: #fff;
  cursor: pointer;
  line-height: 45px;
  text-align: center;
}
.write-content input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  clear: rect(0, 0, 0, 0);
  overflow: hidden;
  border: 0;
}
</style>
