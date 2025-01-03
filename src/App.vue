<template>
  <HeaderComponent/>
  <HomeComponent/>
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue'
import HomeComponent from './components/HomeComponent.vue'

export default {
  name: 'App',
  components: {
    HomeComponent,
    HeaderComponent
  }
}
</script>

<style>
/*
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
*/
#app {
  background-image: url("./assets/background.png");
  background-repeat: no-repeat;
  background-size: cover;
  min-height: 100vh;
  padding-bottom: 100px;
}
.bg-gradient-silentguard {
  background: rgb(10,22,26);
  background: linear-gradient(90deg, rgba(10,22,26,1) 0%, rgba(51,110,128,1) 100%);
}
.bg-lightblue-silentguard {
  background-color: rgba(51,110,128,1);
}
.bg-midblue-silentguard {
  background-color: rgba(29,62,73,1);
}
.bg-darkblue-silentguard {
  background-color: rgba(10,22,26,1);
}
.text-midblue-silentguard {
  color: rgba(29,62,73,1);
}

thead {
  background-color: rgba(29,62,73,1);
}
table {
  border-color: rgba(29,62,73,1) !important;
}
table>tbody>tr:not(:last-child)>td{
  border-bottom: 1px solid rgba(29,62,73,1) !important;
}
table>thead>tr>th:not(:last-child){
  border-right: 1px solid #fff !important;
}
table>tbody>tr>td:not(:last-child){
  border-right: 1px solid rgba(29,62,73,1) !important;
}
</style>
