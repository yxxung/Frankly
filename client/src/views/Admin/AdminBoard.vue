<template>
  <div class="container">
    <div style="width: 50%;  padding-right : 30px;  float: left">
      <br /><br />
      <h2> User Management </h2>
      <div class="input-group" style="margin-bottom: 10px">
          <input
          type="text"
          class="form-control"
          placeholder="이름"
          v-model="name"
          @keyup.enter="createUser(name)"
        />                <input
          type="text"
          class="form-control"
          placeholder="나이"
          v-model="age"
          @keyup.enter="createUser(age)"
        />                <input
          type="text"
          class="form-control"
          placeholder="성별"
          v-model="sex"
          @keyup.enter="createUser(sex)"
        />
      </div>
                   <span class="input-group-btn"
        >                <button
          class="btn btn-success"
          type="button"
          @click="createUser(str)"
        >
           추가 </button
        >            </span
      >
      <div v-if="isModify">
                        <input
          type="text"
          class="form-control"
          placeholder="이름"
          v-model="modifyName"
          @keyup.enter="modifyUser(modifyName)"
        />                <input
          type="text"
          class="form-control"
          placeholder="나이"
          v-model="modifyAge"
          @keyup.enter="modifyUser(modifyAge)"
        />                <input
          type="text"
          class="form-control"
          placeholder="성별"
          v-model="modifySex"
          @keyup.enter="modifyUser(modifySex)"
        />                <button
          class="btn btn-success"
          type="button"
          @click="modifyUser(modifyStr)"
        >
           수정완료 </button
        >
      </div>
                  <br />
      <ul class="list-group">

        <li
          class="list-group-item"
          v-for="(user, index) in pageUsers[curpageNumber]"
        >
                              <strong>이름 : </strong
          >{{ user.name }} <strong>　　나이 : </strong> {{
            user.age
          }} <strong>　　성별 : </strong> {{ user.sex }}
          <div
            class="btn-group pull-right"
            style="font-size: 12px;  line-height: 1"
          >
                                    <button
              type="button"
              class="btn-link dropdown-toggle"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
                                          더보기 <span class="caret"></span
              >                        </button
            >
            <ul class="dropdown-menu">

              <li><a href="#" @click="modifyUser(index)"> 수정 </a></li>

              <li><a href="#" @click="deleteUser(index)"> 삭제 </a></li>

            </ul>

          </div>

        </li>

      </ul>
                  <button
        type="button"
        class="btn btn-warning"
        @click="pagePrev"
      >
        ◀ prev</button
      >            <button
        type="button"
        class="btn btn-warning"
        @click="pageNext"
      >
        next ▶</button
      >
    </div>

    <div style="width: 50%;  padding-left : 30px;  float: right">

      <div class="btn-group">
                        <button
          type="button"
          class="btn btn-primary"
          @click="searchOn"
        >
          검색</button
        >                <button
          type="button"
          class="btn btn-primary"
          @click="filterOn"
        >
          필터링</button
        >
      </div>

      <div v-if="isSearch">

        <h2> Search </h2>

        <div class="input-group" style="margin-bottom: 10px">
                              <input
            type="text"
            class="form-control"
            placeholder="이름"
            v-model="searchName"
            @keyup.enter="searchUser(searchName)"
          />                    <input
            type="text"
            class="form-control"
            placeholder="나이"
            v-model="searchAge"
            @keyup.enter="searchUser(searchAge)"
          />                    <input
            type="text"
            class="form-control"
            placeholder="성별"
            v-model="searchSex"
            @keyup.enter="searchUser(searchSex)"
          />
        </div>
                         <span class="input-group-btn"
          >                    <button
            class="btn btn-info"
            type="button"
            @click="searchUser(str)"
          >
             검색 </button
          >                </span
        >                <br />
        <ul class="list-group">

          <li class="list-group-item" v-for="(user, index) in searchUsers">
                                    <strong>이름 : </strong
            >{{ user.name }} <strong>　　나이 : </strong> {{
              user.age
            }} <strong>　　성별 : </strong> {{ user.sex }}
          </li>

        </ul>

      </div>

      <div v-if="!isSearch">

        <h2> Filtering </h2>

        <div class="input-group" style="margin-bottom: 10px">

          <div class="input-group" style="margin-bottom: 10px;  width: 540px">
                                <input
              type="text"
              class="form-control"
              placeholder="이곳에 입력하세요."
              v-model="filterText"
            />
          </div>

        </div>

        <ul class="list-group">

          <li class="list-group-item" v-for="(user, index) in filterUsers">
                                    <strong>이름 : </strong
            >{{ user.name }} <strong>　　나이 : </strong> {{
              user.age
            }} <strong>　　성별 : </strong> {{ user.sex }}
          </li>

        </ul>

      </div>

    </div>

  </div>
</template>
<script>
export default {
  name: 'Admin',
  props: ['msg'],
  data(){
    return {
      str:{
        name:null,
        age:null,
        sex:null,
        },

        name:null,
        age:null,
        sex:null,
        users: [
          {
            name:"고관우",
            age:"27",
            sex:"남",
          },
          {
            name:"abc",
            age:"28",
            sex:"남",
          },
          {
            name:"고고고",
            age:"39",
            sex:"여",
          }
        ],

        isModify: false,
        modifyStr:{
          name:null,
          age:null,
          sex:null,
        },

        modifyName:null,
        modifyAge:null,
        modifySex:null,
        modifyIdx:null,
        isSearch:true,

        searchStr:{
          name:null,
          age:null,
          sex:null,
        },

        searchName:null,
        searchAge:null,
        searchSex:null,

        searchUsers: [],

        filterText:null,
        filterUsers: [],

        usersNumber: 0, // 이거는 나중에 수정하기
        curpageNumber: 1,
        maxpageNumber: 1,
        pageUsers: [[]],
        }
        },
        created() {
          this.usersNumber = this.users.length;
          this.pageUsers = [[]];
          this.maxpageNumber = this.usersNumber / 10 + 1;

          for(var i = 0; i < this.maxpageNumber; i++)
          this.pageUsers.push([]);
          var page = 1;
          var num = 0;

          for(var i = 0; i < this.usersNumber; i++)
          {
            this.pageUsers[page].push(this.users[i]);
            num++;
            if(num == 10)
            {
              num = 0;
              page++;
            }
          }
        },
        methods: {
          deleteUser:function(index)
          {
            this.users.splice(index,1);
            this.usersNumber--;
          },
          createUser:function(val)
          {
            this.users.push({ name: val.name, age: val.age, sex: val.sex });
            this.usersNumber++;
            this.pageUsers = [[]];
            this.maxpageNumber = this.usersNumber / 10 + 1;

            for(var i = 0; i < this.maxpageNumber; i++)
            this.pageUsers.push([]);
            var page = 1;
            var num = 0;

            for(var i = 0; i < this.usersNumber; i++)
            {
              this.pageUsers[page].push(this.users[i]);
              num++;
              if(num == 10){
                num = 0;
                page++;
              }
            }
          },
          modifyUser:function(val)
          {
            if(!this.isModify)
            {
              this.isModify = true;
              this.modifyIdx = val;
            }
            else
            {
              if(val.name === undefined || val.age === undefined || val.sex === undefined)
              {
                this.modifyIdx = val;
                return;
              }
              this.users[this.modifyIdx] = { name: val.name, age: val.age, sex: val.sex };
              this.isModify = false;
              this.modifyName = null;
              this.modifyAge = null;
              this.modifySex = null;
              this.modifyIdx = null;
              }
              this.setUsers();
          },
          searchOn:function()
          {
            this.isSearch = true;
          },
          searchUser:function()
          {
            this.searchUsers = [];
            var JSONstr = JSON.stringify(this.searchStr);

            for(var i = 0 ; i < this.users.length; i++)
            {
              var JSONusers = JSON.stringify(this.users[i]);
              if(JSONstr === JSONusers)
              {
                this.searchUsers.push(this.users[i]);
              }
            }
          },
          filterOn:function()
          {
            this.isSearch = false;
          },
          pagePrev:function()
          {
            if(this.curpageNumber - 1 > 0)
            this.curpageNumber--;
          },
          pageNext:function()
          {
            if(this.curpageNumber + 1 <= this.maxpageNumber)
            this.curpageNumber++;
          },
          setUsers:function()
          {
            this.pageUsers = [[]];
            this.maxpageNumber = this.usersNumber / 10 + 1;
            for(var i = 0; i < this.maxpageNumber; i++)
            this.pageUsers.push([]);
            var page = 1;
            var num = 0;
            for(var i = 0; i < this.usersNumber; i++)
            {
              this.pageUsers[page].push(this.users[i]);
              num++;
              if(num == 10){
                num = 0;
                page++;
              }
            }
          }
        },
        watch: {
          name:function() {
            this.str.name = this.name;
          },
          age:function() {
            this.str.age = this.age;
          },
          sex:function(){
            this.str.sex = this.sex;
          },
          modifyName:function() {
            this.modifyStr.name = this.modifyName;
          },
          modifyAge:function() {
            this.modifyStr.age = this.modifyAge;
          },
          modifySex:function() {
            this.modifyStr.sex = this.modifySex;
          },
          searchName:function() {
            this.searchStr.name = this.searchName;
          },
          searchAge:function(){
            this.searchStr.age = this.searchAge;
          },
          searchSex:function(){
            this.searchStr.sex = this.searchSex;
          },
          filterText:function(){
            this.filterUsers=[];
            if(this.filterText === '')
            return;

            for(var i = 0 ; i < this.users.length; i++){
              if(this.users[i].name === undefined || this.users[i].age === undefined || this.users[i].sex === undefined)
              continue;
              if(this.users[i].name === null || this.users[i].age === null || this.users[i].sex === null)
              continue;
              if(this.users[i].name.includes(this.filterText) || this.users[i].age.includes(this.filterText) || this.users[i].sex.includes(this.filterText))
              {
                this.filterUsers.push(this.users[i]);
              }
            }
          },
          users:function(){
            this.pageUsers = [[]];
            this.maxpageNumber = this.usersNumber / 10 + 1;
            for(var i = 0; i < this.maxpageNumber; i++)
              this.pageUsers.push([]);

            var page = 1;
            var num = 0;
            for(var i = 0; i < this.usersNumber; i++)
            {
              this.pageUsers[page].push(this.users[i]);
              num++;
              if(num == 10){
                num = 0;
                page++;
              }
            }
          }
        }
      }
</script>
