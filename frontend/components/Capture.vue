<template>
  <v-layout row wrap>
    <v-container grid-list-xl>
      <v-card>
        <div class="text-center">
          <canvas id="canvas" width="1280" height="960" style="display:none;"/>
          <video id="video" width="100%" height="50%" autoplay/>

          <v-overlay :absolute="absolute" :value="overlay">
            <InfoCard></InfoCard>
            <v-btn color="success" @click="overlay = false" block>
              Scan Again
            </v-btn>
          </v-overlay>
        </div>

        <v-btn @click.native="process" color="primary" block>Click to Scan</v-btn>
        <v-btn color="success" @click="overlay = !overlay" block>
          Show Overlay
        </v-btn>
      </v-card>
    </v-container>

    <!--<v-icon left></v-icon> Analyze</v-btn>-->
    <!--<h4 class="red--text">You should: {{resultText}} it!</h4>-->
  </v-layout>
  <!--
  <v-layout row wrap>
    <v-flex xs12 sm12 md6 lg6 xl6>
      <v-card>
        <video id="video" width="100%" height="50%" autoplay></video>
      </v-card>

      <canvas id="canvas" width="200%" height="50%"></canvas>
      <v-btn @click.native="process" block secondary dark>Analyze</v-btn>

    </v-flex>
    <v-flex xs12 sm12 md6 lg6 xl6>
      <h2 class="orange--text text-xs-center">Result</h2>
      <h4 class="red--text">You should: {{resultText}} it!</h4>
      <h4>I see...</h4>
    </v-flex>
  </v-layout>
  -->
</template>

<script>

  import axios from 'axios';
  import InfoCard from "./InfoCard";
  import Stats from "./Stats";
  export default {
    components: {Stats, InfoCard},
    data(){

      return{
        absolute: true,
        overlay: false,
        loader: false,
        label: null,
        action: null,
        data: {               //type vision api Request
          "requests": [{
            "features": [{
              "type": "LABEL_DETECTION"
            }],
            "image": {
              "content": null
            }
          }]
        }
      }
    },
    methods: {
      process() {
        const canvas = document.getElementById('canvas');
        const context = canvas.getContext('2d');
        const video = document.getElementById('video');

        const constraints = {
          video: true,
        };


        // Attach the video stream to the video element and autoplay.
        navigator.mediaDevices.getUserMedia(constraints)
          .then((stream) => {
            video.srcObject = stream;
          });

        this.result = false;
        this.loader = true;
        context.drawImage(video, 0, 0, 1280, 960);

        const base64 = canvas.toDataURL();
        const finalImage = base64.replace("data:image/png;base64,", "");

        axios.post(`https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDgcSJUpJdAJpR-BAPSEgJU8er57esot2w`,
          this.data).then(response => {

          const labels = response.data.responses[0].labelAnnotations;
          console.log(labels);

          axios.post('https://flask-nuxt-ci.appspot.com/image', {
            payload: labels
          }).then(processedJSON => {
            console.log(processedJSON.data)
            this.label = processedJSON.data[0];
            this.action = processedJSON.data[1];
          })

        }).catch(error => {
          console.log(error);
        })

        this.data.requests[0].image.content = finalImage;
      },
      confidenceInt(num){
        const dig = num.toFixed(2);
        if(dig == 1.0){
          return 100;
        }else{
          const str = dig.toString();
          return str.substring(2, 4);
        }
      }
    }
  };

</script>

<style scoped>

</style>
