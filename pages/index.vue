<style> 

.header-bar {
  background-color:#9BDEF0; /* Light blue */
  padding: 15px;
  text-align: center;
  font-size: 24px;
  font-weight: bold;
}

</style>

<template>
    <div>
      <div class="header-bar">
        <h1>Pathology heatmap generator</h1>
      </div>
      
      <div v-for = "button in buttons" :key="button.label">
        <Button :buttonClass="button.class" @click="button.action"> <FontAwesomeIcon :icon="button.icon" class="fa-icon" />
          {{ button.label }}
        </Button>
      </div>
    </div>
</template>


<script>
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faSearchPlus, faSearchMinus, faUndo, faRedo, faExpand, faPowerOff, faInfo } from '@fortawesome/free-solid-svg-icons'

/* Register the icons into the library */
library.add(faSearchPlus, faSearchMinus, faUndo, faRedo, faExpand, faPowerOff, faInfo)


export default {
    components: {
      FontAwesomeIcon
    },

    data() {
        return {
            buttons: [
              { label: "Zoom In", class: "secondary", action: this.zoomIn, icon: "search-plus" },
              { label: "Zoom Out", class: "secondary", action: this.zoomOut, icon: "search-minus" },
              { label: "Rotate Left", class: "secondary", action: this.rotateLeft, icon: "undo" },
              { label: "Rotate Right", class: "secondary", action: this.rotateRight, icon: "redo"},
              { label: "Full Screen", class: "secondary", action: this.fullScreen, icon: "expand" },
              { label: "Toggle heatmap", class: "success", action: this.toggleHeatmap, icon: "power-off" },
              { label: "Info", class: "secondary", action: this.showInfo, icon: "info" },
            ]
        };
    },

    methods: {
        zoomIn() {
        alert("Zooming In!");
        },
        zoomOut() {
        alert("Zooming Out!");
        },
        rotateLeft() {
        alert("Rotating Left!");
        },
        rotateRight() {
        alert("Rotating Right!");
        },
        fullScreen() {
        alert("Full Screen!");
        },
        toggleHeatmap() {
        alert("Toggle Heatmap!");
        },
        showInfo() {
        alert("Show info!");
        }
    }
};
</script>
<template>
    <div>
        <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
    </div>
</template>

<script lang="ts">
import('openseadragon').then(OpenSeadragon => {
    const viewer = OpenSeadragon.default({
        id: "openseadragon1",
        preserveViewport: true,
        visibilityRatio: 1,
        minZoomLevel: 1,
        defaultZoomLevel: 1,
        sequenceMode: true,
        tileSources:
            [
                {
                    '@context': 'http://iiif.io/api/image/2/context.json',
                    '@id': 'https://libimages1.princeton.edu/loris/pudl0001%2F4609321%2Fs42%2F00000001.jp2',
                    height: 7200,
                    width: 5233,
                    profile: ['http://iiif.io/api/image/2/level2.json'],
                    protocol: 'http://iiif.io/api/image',
                    tiles: [
                        {
                            scaleFactors: [1, 2, 4, 8, 16, 32],
                            width: 1024
                        }
                    ]
                }
            ]
    });
});
</script>
