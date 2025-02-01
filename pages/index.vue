<style>
.header-bar {
    padding: 10px;
    text-align: center;
    font-family: 'Courier New', Courier, monospace;
    font-size: 24px;
    font-weight: bold;
}

body {
  background-color: #F2F2EB; /* Light grey background */
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
</style>

<script lang="ts">
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faSearchPlus, faSearchMinus, faUndo, faRedo, faExpand, faPowerOff, faInfo } from '@fortawesome/free-solid-svg-icons'
import { Style } from '#components';

/* Register the icons into the library */
library.add(faSearchPlus, faSearchMinus, faUndo, faRedo, faExpand, faPowerOff, faInfo)

export default {
    components: {
        FontAwesomeIcon
    },

    data() {
        return {
            buttons: [
                // { label: "Zoom In", class: "secondary", action: this.zoomIn, icon: "search-plus" },
                // { label: "Zoom Out", class: "secondary", action: this.zoomOut, icon: "search-minus" },
                // { label: "Rotate Left", class: "secondary", action: this.rotateLeft, icon: "undo" },
                // { label: "Rotate Right", class: "secondary", action: this.rotateRight, icon: "redo" },
                // { label: "Full Screen", class: "secondary", action: this.fullScreen, icon: "expand" },
                { label: "Toggle heatmap", class: "success", action: this.toggleHeatmap, icon: "power-off" },
                // { label: "Info", class: "secondary", action: this.showInfo, icon: "info" },
            ]
        };
    },

    methods: {
        // toggleHeatmap() {
        //     alert("Toggle Heatmap!");
        //     viewer.updateOverlay('openseadragon1', !viewer.getOverlayVisible('heatmap_overlay'));
        // }
    }
};

var slide_name = '17229.svs';
var slide_path = '/Research_1/Prof_Quirke/TISSUE_BANK/GIFT_16/17229.svs';
var slide_width = 32016;
var slide_height = 32731;
var slide_tile = 512;

import('openseadragon').then(OpenSeadragon => {

    const viewer = OpenSeadragon.default({
        id: "openseadragon1",
        preserveViewport: true,
        visibilityRatio: 1,
        minZoomLevel: 1,
        defaultZoomLevel: 1,
        sequenceMode: true,

        overlays: [{
            id: 'right-arrow-overlay',
            x: 100,
            y: 100,
            width: 1000,
            height: 1000,
            placement: 'RIGHT',
            checkResize: false
        }],

        tileSources: {
            debugMode: false,
            crossOriginPolicy: 'Anonymous',
            ajaxWithCredentials: false,
            height: slide_height,
            width: slide_width,
            tileSize: slide_tile,
            minLevel: 0,
            maxLevel: 8,
            getTileUrl: function (level, x, y) {

                var zoom_list = [256, 128, 64, 32, 16, 8, 4, 2, 1];
                var zoom = zoom_list[level]; //((max_level + 0) - level) - 1;

                var request_string = "https://slides.virtualpathology.leeds.ac.uk" +
                    slide_path + '?' +
                    ((x * slide_tile)) + '+' +
                    ((y * slide_tile)) + '+' +
                    slide_tile + '+' +
                    slide_tile + '+' +
                    zoom + //1 / (level - (slide_levels - 1)) +
                    '+100';

                // console.log(request_string);

                return request_string;
            }
        }
    });

    const button = new OpenSeadragon.Button({
    tooltip: 'Toggle heatmap',
    srcRest: 'https://openseadragon.github.io/openseadragon/images/zoom-in_rest.png',
    srcGroup: 'https://openseadragon.github.io/openseadragon/images/zoom-in_grouphover.png',
    srcHover: 'https://openseadragon.github.io/openseadragon/images/zoom-in_hover.png',
    srcDown: 'https://openseadragon.github.io/openseadragon/images/zoom-in_pressed.png',
    onClick: function () {
        const overlay = viewer.getOverlayById('example-overlay');
        if (overlay) {
            viewer.removeOverlay('example-overlay');
        } else {
            const overlayElement = document.createElement("img");
            overlayElement.id = "example-overlay";
            overlayElement.style.padding = "10px";
            overlayElement.src = "https://upload.wikimedia.org/wikipedia/commons/b/b9/Solid_red.png";
            overlayElement.style.width = "100%";
            overlayElement.style.height = "100%";
            overlayElement.style.opacity = "0.2";


            viewer.addOverlay({
                element: overlayElement,
                location: new OpenSeadragon.Rect(0, 0, 1, 1)
            });
        }
    }
});

    viewer.addControl(button.element, { anchor: OpenSeadragon.ControlAnchor.TOP_LEFT });
    
//     viewer.addHandler("canvas-drag", function () {
//         console.log("Hello");
//         var overlay = document.createElement("div");
//         overlay.id = "example-overlay";
//         overlay.innerHTML = "This is an overlay";
//         overlay.style.background = "rgba(255, 255, 255, 0)";
//         overlay.style.padding = "10px";
//         overlay.style.fontFamily = "Arial, sans-serif";

//         viewer.addOverlay({
//             element: overlay,
//             location: new OpenSeadragon.Rect(0.1, 0.1, 0.3, 0.2)
//         });
//     });
});

function test() {
    console.log("Hello");
}

</script>

<template>
    <div class="header-bar">
        <h1>Pathology heatmap generator</h1>
    </div>

    <div class="button-container">
      <div v-for="button in buttons" :key="button.label">
        <Button :buttonClass="button.class" @click="button.action">
            <FontAwesomeIcon :icon="button.icon" class="fa-icon" />
            {{ button.label }}
        </Button>
      </div>
    </div>

    <div id="custom-overlay" class="overlay" style="display: none;">This is an overlay</div>

    <div>
        <div @click="test">
            test
        </div>
        <div id="openseadragon1" class="p-4 h-screen"></div>
    </div>
</template>
