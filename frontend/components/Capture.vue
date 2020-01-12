<template>
  <v-layout row wrap>
    <v-container grid-list-xl>
      <v-card>
        <!-- logo -->
        <v-card-actions class="justify-center">
          <custom-logo></custom-logo>
          <stats/>
        </v-card-actions>

        <div class="text-center">
          <canvas id="canvas" width="100%" height="50%" style="display:none;"/>
          <video id="video" width="100%" height="50%" autoplay/>

          <v-overlay :absolute="absolute" :value="overlay">
            <InfoCard></InfoCard>
            <v-btn color="success" @click="overlay = false" block>
              Scan Again
            </v-btn>
          </v-overlay>


          <!--
          <v-overlay :absolute="absolute" :value="overlay">
            <InfoCard></InfoCard>
          </v-overlay>
          -->
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

  //import $ from "jquery";
  import axios from 'axios';
  import CustomLogo from "./CustomLogo";
  import InfoCard from "./InfoCard";
  import Stats from "./Stats";
  export default {
    components: {Stats, InfoCard, CustomLogo},
    data(){

      return{
        absolute: true,
        overlay: false,
        loader: false,
        result: false,
        resultText: null,
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
        context.drawImage(video, 0, 0, 640, 480);

        const base64 = canvas.toDataURL();
        const finalImage = base64.replace("data:image/png;base64,", "");

        /*
        axios.post(`https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDgcSJUpJdAJpR-BAPSEgJU8er57esot2w`,
          this.data).then(response => {
          console.log(response);
        }).catch(error => {
          console.log(error);
        })
        */


        axios.post(`https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDgcSJUpJdAJpR-BAPSEgJU8er57esot2w`,
          this.data).then(response => {

            const result = response.data.responses[0];
            console.log(result);

            //const [result] = await client.labelDetection('./resources/wakeupcat.jpg');
            const labels = result.labelAnnotations;
            console.log(labels);

            axios.post('http://127.0.0.1:5000/image', {
              payload: labels
            }).then(action => {
              console.log(action)
              this.resultText = action.data;
            })


            /*
            const result = response.data.responses[0];
            console.log(result);
            */
          /*
          const result = response.data.responses[0].faceAnnotations[0];

          vm.anger = result.angerLikelihood;
          vm.blur = result.blurredLikelihood;
          vm.headwear = result.headwearLikelihood;
          vm.joy = result.joyLikelihood;
          vm.sorrow = result.sorrowLikelihood;
          vm.surprised = result.surpriseLikelihood;
          vm.confidence = this.confidenceInt(result.detectionConfidence);
          vm.loader = false;
          vm.result = true;
*/




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
