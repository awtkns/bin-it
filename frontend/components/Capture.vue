<template>
  <v-layout row wrap>
    <v-flex xs12 sm12 md6 lg6 xl6>
      <v-card>
        <video id="video" width="100%" height="50%" autoplay></video>
        <canvas id="canvas" width="600" height="480" style="background-color: blue;"></canvas>

        <!--
        <script>
          //
          // if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          //   navigator.mediaDevices.getUserMedia({
          //     video: true
          //   }).then(stream => {
          //     video.src = window.URL.createObjectURL(stream);
          //     video.play();
          //   });
          // }
        </script>
        -->
      </v-card>
      <v-btn @click.native="process" block secondary dark>
        <v-icon left>camera_alt</v-icon> Analyze</v-btn>
    </v-flex>
    <v-flex xs12 sm12 md6 lg6 xl6>
      <h2 class="orange--text text-xs-center">Result</h2>
      <div class="text-xs-center" v-show="loader">
        <v-progress-circular indeterminate v-bind:size="100" v-bind:width="3" class="teal--text"></v-progress-circular>
      </div>
      <div v-show="result" class="text-md-center">
        <h4 class="red--text">You should: {{ resultText }} it!%</h4>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>

  //import $ from "jquery";
  import axios from 'axios';
  export default {
    data(){
      return{
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

        const vm = this;
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
