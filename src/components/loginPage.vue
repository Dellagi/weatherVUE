<template>
  <v-container fluid fill-height>
    <v-layout align- justify-center>
    <v-row class="text-center" align="center">



      <v-col
        class="rounded-lg"
        cols="12"
        id='loginForm'
      >
      <v-card color="#F8F8FF">
        <h2 v-if="signIn" class="headline font-weight-bold mb-3 ">
        Sign In 
        </h2>
        <h2 v-else class="headline font-weight-bold mb-3 ">
        Sign Up 
        </h2>
        <v-divider></v-divider>
        <v-card-text>
        <v-form
          ref="form"
        >
          <v-text-field
            v-model="name"
            label="Name"
            required
          ></v-text-field>

          <v-text-field
            v-model="pass"
            :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="() => (value = !value)"
            :type="value ? 'password' : 'text'"
            :value="myPass"
            label="Password"
            required
          ></v-text-field>

<div v-if="!signIn">
<v-autocomplete  v-model="chosencountry" @change="getcity(chosencountry)"
        class="mx-16 my-16"
      :items="country"
      label="Country"
      item-text="code"
      item-value="code"
      >
</v-autocomplete>
<v-autocomplete v-model="chosencity" @change="complete=1"
        class="mx-16 my-16"
      :items="city"
      label="city"
      item-text="name"
      item-value="name"
      >
</v-autocomplete>
</div>


<div v-if="connected && signIn">
  <p>Try again! </p>
</div>

          <v-btn
            color="success"
            class="mr-4"
            @click="valid"
          >
            Validate
          </v-btn>
        </v-form>
      </v-card-text>
      </v-card>
<div v-if="signIn">
        <v-btn
        plain
        @click="signIn= !signIn"
      >
        Sign Up
      </v-btn>
</div>
<div v-else>
        <v-btn
        plain
        @click="signIn= !signIn"
      >
        Sign In
      </v-btn></div>
      </v-col>
    </v-row>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
import qs from 'qs';
  export default {
    name: 'loginPage',
    props:['connected'],
    methods:{
        valid(e){
            e.preventDefault();
            if ( this.signIn){
            const inf = {
                name: this.name,
                pass:this.pass,

            }
            this.$emit('log', inf);
            this.name='';
            this.pass='';
            this.complete=null;

        }},
    getinfo(chosencity,chosencountry){ 
      axios.post('http://localhost:5000/minute',qs.stringify({'chosencity':chosencity,'chosencountry':chosencountry}))
        .then(res => this.chartdata=eval(res.data))
        .catch(err => {console.log(err)});
      
    },

    getcity(chosencountry){
      axios.post('http://localhost:5000/city',qs.stringify({chosencountry}))
        .then(res => this.city =eval(res.data ))
        .catch(err => console.log(err))
    }        
    },
    data: () => ({
      complete:null,
      chartdata:null,
      city:[],
      chosencountry:null,
      chosencity:null,
      er:null,
      country:[{"code": "IR"}, {"code": "SY"}, {"code": "CY"}, {"code": "YE"}, {"code": "RW"}, {"code": "SO"}, {"code": "LY"}, {"code": "IQ"}, {"code": "SA"}, {"code": "AO"}, {"code": "GB"}, {"code": "AZ"}, {"code": "TZ"}, {"code": "TM"}, {"code": "AM"}, {"code": "ZM"}, {"code": "KE"}, {"code": "CD"}, {"code": "DJ"}, {"code": "UG"}, {"code": "MW"}, {"code": "CF"}, {"code": "SC"}, {"code": "TD"}, {"code": "JO"}, {"code": "GR"}, {"code": "LB"}, {"code": "PS"}, {"code": "IL"}, {"code": "KW"}, {"code": "OM"}, {"code": "QA"}, {"code": "BH"}, {"code": "AE"}, {"code": "TR"}, {"code": "ET"}, {"code": "ER"}, {"code": "EG"}, {"code": "AL"}, {"code": "SD"}, {"code": "SS"}, {"code": "BI"}, {"code": "FI"}, {"code": "RU"}, {"code": "EE"}, {"code": "BG"}, {"code": "UZ"}, {"code": "LV"}, {"code": "UA"}, {"code": "GE"}, {"code": "LT"}, {"code": "SE"}, {"code": "KZ"}, {"code": "BY"}, {"code": "MD"}, {"code": "AX"}, {"code": "RO"}, {"code": "HU"}, {"code": "MK"}, {"code": "SK"}, {"code": "PL"}, {"code": "NO"}, {"code": "RS"}, {"code": "XK"}, {"code": "ME"}, {"code": "NA"}, {"code": "ZW"}, {"code": "KM"}, {"code": "YT"}, {"code": "LS"}, {"code": "BW"}, {"code": "MU"}, {"code": "SZ"}, {"code": "RE"}, {"code": "ZA"}, {"code": "MZ"}, {"code": "MG"}, {"code": "PK"}, {"code": "TH"}, {"code": "AF"}, {"code": "IN"}, {"code": "BD"}, {"code": "ID"}, {"code": "TJ"}, {"code": "MY"}, {"code": "KG"}, {"code": "LK"}, {"code": "BT"}, {"code": "CN"}, {"code": "MV"}, {"code": "NP"}, {"code": "MM"}, {"code": "MN"}, {"code": "TF"}, {"code": "CC"}, {"code": "PW"}, {"code": "VN"}, {"code": "TL"}, {"code": "LA"}, {"code": "TW"}, {"code": "PH"}, {"code": "HK"}, {"code": "BN"}, {"code": "MO"}, {"code": "KH"}, {"code": "KR"}, {"code": "JP"}, {"code": "KP"}, {"code": "SG"}, {"code": "CK"}, {"code": "AU"}, {"code": "CX"}, {"code": "MH"}, {"code": "FM"}, {"code": "PG"}, {"code": "SB"}, {"code": "KI"}, {"code": "TV"}, {"code": "NR"}, {"code": "VU"}, {"code": "NC"}, {"code": "NF"}, {"code": "NZ"}, {"code": "FJ"}, {"code": "CM"}, {"code": "SN"}, {"code": "CG"}, {"code": "PT"}, {"code": "LR"}, {"code": "CI"}, {"code": "GH"}, {"code": "GQ"}, {"code": "NG"}, {"code": "BF"}, {"code": "TG"}, {"code": "GW"}, {"code": "MR"}, {"code": "BJ"}, {"code": "GA"}, {"code": "SL"}, {"code": "ST"}, {"code": "SH"}, {"code": "GI"}, {"code": "GM"}, {"code": "GN"}, {"code": "NE"}, {"code": "ML"}, {"code": "EH"}, {"code": "TN"}, {"code": "DZ"}, {"code": "ES"}, {"code": "IT"}, {"code": "MA"}, {"code": "MT"}, {"code": "AT"}, {"code": "DK"}, {"code": "FO"}, {"code": "IS"}, {"code": "IE"}, {"code": "CH"}, {"code": "SJ"}, {"code": "NL"}, {"code": "BE"}, {"code": "DE"}, {"code": "LU"}, {"code": "FR"}, {"code": "MC"}, {"code": "AD"}, {"code": "LI"}, {"code": "JE"}, {"code": "IM"}, {"code": "GG"}, {"code": "CZ"}, {"code": "VA"}, {"code": "SM"}, {"code": "HR"}, {"code": "BA"}, {"code": "SI"}, {"code": "BB"}, {"code": "CV"}, {"code": "GY"}, {"code": "GF"}, {"code": "SR"}, {"code": "BR"}, {"code": "GL"}, {"code": "PM"}, {"code": "GS"}, {"code": "FK"}, {"code": "AR"}, {"code": "PY"}, {"code": "UY"}, {"code": "BO"}, {"code": "VE"}, {"code": "MX"}, {"code": "JM"}, {"code": "DO"}, {"code": "BQ"}, {"code": "CW"}, {"code": "SX"}, {"code": "CU"}, {"code": "MQ"}, {"code": "BS"}, {"code": "BM"}, {"code": "AI"}, {"code": "TT"}, {"code": "KN"}, {"code": "DM"}, {"code": "AG"}, {"code": "LC"}, {"code": "TC"}, {"code": "AW"}, {"code": "VG"}, {"code": "VC"}, {"code": "MS"}, {"code": "GP"}, {"code": "MF"}, {"code": "BL"}, {"code": "GD"}, {"code": "KY"}, {"code": "BZ"}, {"code": "SV"}, {"code": "GT"}, {"code": "HN"}, {"code": "NI"}, {"code": "CR"}, {"code": "EC"}, {"code": "CO"}, {"code": "PE"}, {"code": "PA"}, {"code": "HT"}, {"code": "CL"}, {"code": "PF"}, {"code": "PN"}, {"code": "TK"}, {"code": "TO"}, {"code": "WF"}, {"code": "WS"}, {"code": "NU"}, {"code": "GU"}, {"code": "MP"}, {"code": "US"}, {"code": "PR"}, {"code": "VI"}, {"code": "AS"}, {"code": "CA"}, {"code": ""}, {"code": "AQ"}],
      signIn:1,  
      connected:0,
      name:'',
      pass:'',
      value: String,
     
    }),
  }
</script>
<style scoped>
#loginForm {
  max-width: 500px;
  margin: auto;
}
</style>