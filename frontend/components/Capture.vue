<template>
  <v-layout row wrap>
    <v-container grid-list-xl>
      <v-card height="550px">
        <div class="text-center">
          <canvas id="canvas" width="1280" height="960" style="display:none;"/>
          <!--<video id="video" autoplay style="position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;"/>-->
          <div style="position: absolute;
                        top: 0;
                        bottom: 0;
                        width: 100%;
                        height: 100%;
                        overflow: hidden;">
            <div>
              <video id="video" autoplay style="min-width: 100%;
                                                min-height: 100%;
                                                width: auto;
                                                height: auto;
                                                position: absolute;
                                                top: 50%;
                                                left: 50%;
                                                transform: translate(-50%, -50%);"/>
              <script>
                const video = document.getElementById('video');

                const constraints = {
                  video: true,
                  facingMode: { exact: "environment" },
                };

                // Attach the video stream to the video element and autoplay.
                navigator.mediaDevices.getUserMedia(constraints)
                  .then((stream) => {
                    video.srcObject = stream;
                  });
              </script>
            </div>
          </div>

          <v-overlay :absolute="absolute" :value="overlay">
            <!--<InfoCard></InfoCard>-->
            <v-card color="white" class="mx-auto" max-width="344" elevation="2">
              <div style="color:black;text-align: left;">
                <v-card-text >
                  <!-- Recycle it! -->
                  <h1>
                    <v-icon color="black" left>mdi-recycle</v-icon>
                    {{action}}
                  </h1>
                </v-card-text>
                <v-card-text>
                  <h2>How to Reuse it?</h2>
                  <br>
                  <p>
                    {{label}}: {{action}}
                  </p>
                </v-card-text>

                <v-card-text>
                  <h2>Whats the Impact?</h2>
                  <br>
                  <p>
                    In addition to reducing greenhouse gas emissions, recycling also helps to decrease the amount of pollution in the air and water sources.
                  </p>
                </v-card-text>

                <v-card-text>
                  <a v-bind:href="''+this.link+''">Find out more about recycling {{label}}s</a>
                </v-card-text>

                <v-card-actions>
                  <v-btn to="/" block rounded style="padding: 25px; color:cornflowerblue;" outlined color="primary">
                    Back to home
                  </v-btn>
                </v-card-actions>

                <v-card-actions>
                  <v-btn color="primary" @click="overlay=false" block rounded style="padding: 25px;">
                    Scan Again
                  </v-btn>
                </v-card-actions>
                <!--
              <v-card-actions>

              </v-card-actions>
              -->
              </div>
            </v-card>

          </v-overlay>

          <v-card-actions class="justify-center" row wrap  align-end style="height: 475px;">

          </v-card-actions>

          <v-card-actions class="justify-center" row wrap  align-end>
            <v-btn href="/" rounded>
              <v-icon dark left>mdi-arrow-left</v-icon>
            </v-btn>

            <v-btn @click.native="process" color="primary" rounded>
              <v-icon center>mdi-camera</v-icon>
            </v-btn>
          </v-card-actions>
        </div>

        <!--<v-btn color="success" @click="overlay = !overlay" block>
          Show Overlay
        </v-btn>-->
      </v-card>
    </v-container>

    <!--<v-icon left></v-icon> Analyze</v-btn>-->
    <!--<h4 class="red--text">You should: {{resultText}} it!</h4>-->
  </v-layout>
</template>

<script>

  import axios from 'axios';
  import InfoCard from "./InfoCard";
  import Stats from "./Stats";
  import CustomLogo from "./CustomLogo";
  export default {
    components: {CustomLogo, Stats, InfoCard},
    data(){
      return{
        absolute: true,
        overlay: false,
        loader: false,
        label: null,
        action: null,
        link: "www.google.ca",
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

        this.overlay = !this.overlay;

        const constraints = {
          video: true,
          facingMode: { exact: "environment" },
        };

        // Attach the video stream to the video element and autoplay.
        navigator.mediaDevices.getUserMedia(constraints)
          .then((stream) => {
            video.srcObject = stream;
          });

        this.loader = true;
        context.drawImage(video, 0, 0, 1280, 960);

        const base64 = canvas.toDataURL();
        const finalImage = base64.replace("data:image/png;base64,", "");

        axios.post(`https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDgcSJUpJdAJpR-BAPSEgJU8er57esot2w`,
          this.data).then(response => {

          const labels = response.data.responses[0].labelAnnotations;
          console.log(labels);

          axios.post('http://127.0.0.1:5000/image', {
            payload: labels
          }).then(processedJSON => {
            console.log(processedJSON.data)
            this.label = processedJSON.data[0];
            this.action = processedJSON.data[1];
            this.link = processedJSON.data[2];
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
