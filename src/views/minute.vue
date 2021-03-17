<template>
    <v-container 
        fluid>
        <v-row>
          <v-col>
            <v-card  width="1000px" class="mx-lg-auto" >



<v-autocomplete  v-model="chosencountry" @change="getcity(chosencountry)"
        class="mx-16 my-16"
      :items="country"
      label="Country"
      item-text="code"
      item-value="code"
      >
</v-autocomplete>
<v-autocomplete v-model="chosencity" @change="getinfo(chosencity,chosencountry)"
        class="mx-16 my-16"
      :items="city"
      label="city"
      item-text="name"
      item-value="name"
      >
</v-autocomplete>


<div v-if="weatherData!=null" class='center' >


            <!-- Weather now-->
        <div class="text-xl-h4 ">{{chosencity}}</div>
        <div class="text-xl-h5 ">{{weatherData[2]['main']['temp']+"°C"}}</div>

       <v-img v-bind:src="linkNow" class="center"  max-height="50" max-width="100 "/>
        <div>{{weatherData[2]['weather'][0]['description']}}</div>

    <v-container>
      <v-row
        class=""
        align="center"
        no-gutters
        style="height: 150px;"
      >
        <v-col
          v-for="n in 3"
          :key="n"
        >
          <v-card
            class="pa-2"
            outlined
          >
{{todayColumns[n-1]}}
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-container>
      <v-row
        class=""
        align="center"
        no-gutters
        style="height: 150px;"
      >
        <v-col
          v-for="n in 3"
          :key="n"
        >
          <v-card
            class="pa-2"
            outlined
          >
{{todayColumns[n+2]}}
          </v-card>
        </v-col>
      </v-row>
    </v-container>

<!--hourly -->
  <div class="text-xl-h6 ">Next 48 hours </div>

  <v-slide-group
      class="pa-4"
    >
      <v-slide-item
        v-for="n in 48"
        :key="n"
      >
        <v-card
          class="ma-4"
          height="200"
          width="100"
          disabled
          elevation="0"
        >
  <div class="text-xl-h6 ">{{weatherData[1]['temp'][n-1]+"°C"}}</div>

  <v-img v-bind:src="linkHourly[n-1]" class="center"  max-height="50" max-width="100 "/>
    <div class="text-xl-h6 ">{{weatherData[1]['weather_description'][n-1]}}</div>


        </v-card>
      </v-slide-item>
    </v-slide-group>


<!--daily -->
  <div class="text-xl-h6 ">Next days</div>




  <v-simple-table>
    <template >
      <thead>
        <tr>
          <th class="text-left"> 
          </th>
          <th class="text-left">
          </th>
          <th class="text-left">
            Lowest temperature
          </th>
          <th class="text-left">
            Highest temperature
          </th>
          <th class="text-left">
            Wind speed
          </th>
          <th class="text-left">
            Cloudiness
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="n in weatherData[0]"
          :key="n.name"
        >
          <td>{{n.day }}</td>
          <td>  <v-img v-bind:src="linkDaily[n.name]" class="center"  max-height="25" max-width="50 "/></td>
          <td>{{n.temp_min+'°C' }}</td>
          <td>{{n.temp_max+'°C' }}</td>
          <td>{{n.wind_sp+'km/h' }}</td>
          <td>{{n.cloud+'%' }}</td>
                  

        </tr>
      </tbody>
    </template>
  </v-simple-table>




          </div>












            </v-card>
          </v-col>
        </v-row>
    </v-container>


</template>
<script>

import axios from 'axios';
import qs from 'qs';


  export default {
    name:'minute',

    data: () => ({
      todayColumns:null,
      weatherData:null,
      linkHourly:[],
      linkDaily:[],
      city:[],
      chosencountry:null,
      chosencity:null,
      er:null,
      country:[{"code": "IR"}, {"code": "SY"}, {"code": "CY"}, {"code": "YE"}, {"code": "RW"}, {"code": "SO"}, {"code": "LY"}, {"code": "IQ"}, {"code": "SA"}, {"code": "AO"}, {"code": "GB"}, {"code": "AZ"}, {"code": "TZ"}, {"code": "TM"}, {"code": "AM"}, {"code": "ZM"}, {"code": "KE"}, {"code": "CD"}, {"code": "DJ"}, {"code": "UG"}, {"code": "MW"}, {"code": "CF"}, {"code": "SC"}, {"code": "TD"}, {"code": "JO"}, {"code": "GR"}, {"code": "LB"}, {"code": "PS"}, {"code": "IL"}, {"code": "KW"}, {"code": "OM"}, {"code": "QA"}, {"code": "BH"}, {"code": "AE"}, {"code": "TR"}, {"code": "ET"}, {"code": "ER"}, {"code": "EG"}, {"code": "AL"}, {"code": "SD"}, {"code": "SS"}, {"code": "BI"}, {"code": "FI"}, {"code": "RU"}, {"code": "EE"}, {"code": "BG"}, {"code": "UZ"}, {"code": "LV"}, {"code": "UA"}, {"code": "GE"}, {"code": "LT"}, {"code": "SE"}, {"code": "KZ"}, {"code": "BY"}, {"code": "MD"}, {"code": "AX"}, {"code": "RO"}, {"code": "HU"}, {"code": "MK"}, {"code": "SK"}, {"code": "PL"}, {"code": "NO"}, {"code": "RS"}, {"code": "XK"}, {"code": "ME"}, {"code": "NA"}, {"code": "ZW"}, {"code": "KM"}, {"code": "YT"}, {"code": "LS"}, {"code": "BW"}, {"code": "MU"}, {"code": "SZ"}, {"code": "RE"}, {"code": "ZA"}, {"code": "MZ"}, {"code": "MG"}, {"code": "PK"}, {"code": "TH"}, {"code": "AF"}, {"code": "IN"}, {"code": "BD"}, {"code": "ID"}, {"code": "TJ"}, {"code": "MY"}, {"code": "KG"}, {"code": "LK"}, {"code": "BT"}, {"code": "CN"}, {"code": "MV"}, {"code": "NP"}, {"code": "MM"}, {"code": "MN"}, {"code": "TF"}, {"code": "CC"}, {"code": "PW"}, {"code": "VN"}, {"code": "TL"}, {"code": "LA"}, {"code": "TW"}, {"code": "PH"}, {"code": "HK"}, {"code": "BN"}, {"code": "MO"}, {"code": "KH"}, {"code": "KR"}, {"code": "JP"}, {"code": "KP"}, {"code": "SG"}, {"code": "CK"}, {"code": "AU"}, {"code": "CX"}, {"code": "MH"}, {"code": "FM"}, {"code": "PG"}, {"code": "SB"}, {"code": "KI"}, {"code": "TV"}, {"code": "NR"}, {"code": "VU"}, {"code": "NC"}, {"code": "NF"}, {"code": "NZ"}, {"code": "FJ"}, {"code": "CM"}, {"code": "SN"}, {"code": "CG"}, {"code": "PT"}, {"code": "LR"}, {"code": "CI"}, {"code": "GH"}, {"code": "GQ"}, {"code": "NG"}, {"code": "BF"}, {"code": "TG"}, {"code": "GW"}, {"code": "MR"}, {"code": "BJ"}, {"code": "GA"}, {"code": "SL"}, {"code": "ST"}, {"code": "SH"}, {"code": "GI"}, {"code": "GM"}, {"code": "GN"}, {"code": "NE"}, {"code": "ML"}, {"code": "EH"}, {"code": "TN"}, {"code": "DZ"}, {"code": "ES"}, {"code": "IT"}, {"code": "MA"}, {"code": "MT"}, {"code": "AT"}, {"code": "DK"}, {"code": "FO"}, {"code": "IS"}, {"code": "IE"}, {"code": "CH"}, {"code": "SJ"}, {"code": "NL"}, {"code": "BE"}, {"code": "DE"}, {"code": "LU"}, {"code": "FR"}, {"code": "MC"}, {"code": "AD"}, {"code": "LI"}, {"code": "JE"}, {"code": "IM"}, {"code": "GG"}, {"code": "CZ"}, {"code": "VA"}, {"code": "SM"}, {"code": "HR"}, {"code": "BA"}, {"code": "SI"}, {"code": "BB"}, {"code": "CV"}, {"code": "GY"}, {"code": "GF"}, {"code": "SR"}, {"code": "BR"}, {"code": "GL"}, {"code": "PM"}, {"code": "GS"}, {"code": "FK"}, {"code": "AR"}, {"code": "PY"}, {"code": "UY"}, {"code": "BO"}, {"code": "VE"}, {"code": "MX"}, {"code": "JM"}, {"code": "DO"}, {"code": "BQ"}, {"code": "CW"}, {"code": "SX"}, {"code": "CU"}, {"code": "MQ"}, {"code": "BS"}, {"code": "BM"}, {"code": "AI"}, {"code": "TT"}, {"code": "KN"}, {"code": "DM"}, {"code": "AG"}, {"code": "LC"}, {"code": "TC"}, {"code": "AW"}, {"code": "VG"}, {"code": "VC"}, {"code": "MS"}, {"code": "GP"}, {"code": "MF"}, {"code": "BL"}, {"code": "GD"}, {"code": "KY"}, {"code": "BZ"}, {"code": "SV"}, {"code": "GT"}, {"code": "HN"}, {"code": "NI"}, {"code": "CR"}, {"code": "EC"}, {"code": "CO"}, {"code": "PE"}, {"code": "PA"}, {"code": "HT"}, {"code": "CL"}, {"code": "PF"}, {"code": "PN"}, {"code": "TK"}, {"code": "TO"}, {"code": "WF"}, {"code": "WS"}, {"code": "NU"}, {"code": "GU"}, {"code": "MP"}, {"code": "US"}, {"code": "PR"}, {"code": "VI"}, {"code": "AS"}, {"code": "CA"}, {"code": ""}, {"code": "AQ"}],
    iconl:{
'thunderstorm with light rain':'11d', 	
'thunderstorm with rain':'11d', 
'thunderstorm with heavy rain':'11d',
'light thunderstorm':'11d', 
'thunderstorm':'11d',
'heavy thunderstorm':'11d',
'ragged thunderstorm':'11d',
'thunderstorm with light drizzle':'11d',
'thunderstorm with drizzle':'11d',
'thunderstorm with heavy drizzle':'11d',

'light intensity drizzle':'09d',
'drizzle':'09d',
'heavy intensity drizzle':'09d',
'light intensity drizzle rain':'09d',
'drizzle rain':'09d',
'heavy intensity drizzle rain':'09d',
'shower rain and drizzle':'09d',
'heavy shower rain and drizzle':'09d',
'shower drizzle':'09d',

'light rain':'10d',
'moderate rain':'10d',
'heavy intensity rain':'10d',
'very heavy rain':'10d',
'extreme rain':'10d',
'freezing rain':'13d',
'light intensity shower rain':'09d',
'shower rain':'09d',
'heavy intensity shower rain':'09d',
'ragged shower rain':'09d', 

'light snow':'13d',
'Snow':'13d',
'Heavy snow':'13d',
'Sleet':'13d',
'Light shower sleet':'13d',
'Shower sleet':'13d',
'Light rain and snow':'13d',
'Rain and snow':'13d',
'Light shower snow':'13d',
'Shower snow':'13d',
'Heavy shower snow':'13d', 

'mist':'50d',
'Smoke':'50d',
'Haze':'50d',
'sand/ dust whirls':'50d',
'fog':'50d',
'sand':'50d',
'dust':'50d',
'volcanic ash':'50d',
'squalls':'50d',
'tornado':'50d',

'clear sky':'01d',
'few clouds':'02d',
'scattered clouds':'03d',
'broken clouds':'04d',
'overcast clouds':'04d'}


    }),

    watch:{
      weatherData:function(val){
        var i;
        var j;
        this.linkNow="http://openweathermap.org/img/wn/" + this.iconl[val[2]['weather'][0]['description']] + "@2x.png";
        for (i = 0; i < 48; i++){ this.linkHourly.push("http://openweathermap.org/img/wn/" + this.iconl[val[1]['weather_description'][i]] + "@2x.png")}
        for (j = 0; j < 8; j++){ this.linkDaily.push("http://openweathermap.org/img/wn/" + this.iconl[val[0][j]['weather']] + "@2x.png")}
        this.todayColumns=[val[2]['main']['pressure'],val[2]['main']['humidity'],val[2]['wind']['speed'],val[2]['wind']['deg'],
        val[2]['clouds']['all'],val[2]['sys']['sunset']]
        
      }
    },

    methods:{ 

    getinfo(chosencity,chosencountry){ 
      axios.post('http://localhost:5000/minute',qs.stringify({'chosencity':chosencity,'chosencountry':chosencountry}))
        .then(res => this.weatherData=eval(res.data))
        .catch(err => {console.log(err)});
      
    },

    getcity(chosencountry){
      axios.post('http://localhost:5000/city',qs.stringify({chosencountry}))
        .then(res => this.city =eval(res.data ))
        .catch(err => console.log(err))
    }
    }

}
</script>
<style scoped>
[class*="center"]{
  margin: auto;
  text-align: center;
}
</style>
