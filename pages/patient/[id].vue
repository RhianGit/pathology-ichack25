<style>
.header-bar {
    font-family: 'Courier New', Courier, monospace;
    font-size: 24px;
    font-weight: bold;
}

/* Dark Mode */
body.dark-mode {
    background-color: #333;
    color: white;
}

body {
    background-color: #F2F2EB;
}

/* Style for the Dark Mode Button */
.dark-mode-button {
    padding: 8px 12px;
    font-size: 16px;
    margin-top: 10px;
    background-color: #333;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-family: 'Courier New', Courier, monospace;
}

.dark-mode-button:hover {
    background-color: #555;
}

body.dark-mode .dark-mode-button {
    background-color: white;
    color: #333;
}

body.dark-mode .dark-mode-button:hover {
    background-color: #ddd;
}
</style>

<script setup lang="ts">
import type OpenSeadragon from 'openseadragon';

let darkMode = false

function toggleDarkMode() {
    darkMode = !darkMode;
    document.body.classList.toggle("dark-mode", darkMode);
}

const route = useRoute()

var slide_path = `/Research_1/Prof_Quirke/TISSUE_BANK/GIFT_16/${route.params.id}.svs`;

let slide_tile = 512;
const slide_id = route.params.id.toString();
let slide_height = 32016;
let slide_width = 32731;

import('openseadragon').then(OpenSeadragon => {
    let overlayVisible = false;

    let options = {
        id: "openseadragon1",
        preserveViewport: true,
        visibilityRatio: 1,
        minZoomLevel: 1,
        defaultZoomLevel: 1,
        sequenceMode: true,

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

                if (overlayVisible) {
                    request_string = 'http://127.0.0.1:5000/transform?' + new URLSearchParams({
                        url: request_string,
                        cb: colorBlindValue.toString(),
                    });
                }

                // console.log(colorBlindValue);
                // console.log(colorBlindValue.toString());

                return request_string;
            }
        }
    };

    let viewer: OpenSeadragon.Viewer | null = null;
    let colorBlindValue = false;

    function colorBlind(): void {
        colorBlindValue = !colorBlindValue;
        reload();
    }

    function reload() {
        let zoom: any | null = null;
        let loc: any | null = null;
        if (viewer !== null) {
            zoom = viewer.viewport.getZoom();
            loc = viewer.viewport.getCenter();
            viewer.destroy();
        }
        viewer = OpenSeadragon.default(options);
        const button = new OpenSeadragon.Button({
            tooltip: '',
            srcRest: '../images/button_rest.png',
            srcHover: '../images/button_hover.png',
            srcDown: '../images/button_down.png',
            onClick: function () {
                overlayVisible = !overlayVisible;
                reload();
            }
        });
        const greyscaleButton = new OpenSeadragon.Button({
            tooltip: '',
            srcRest: '../images/button_rest.png',
            srcHover: '../images/button_hover.png',
            srcDown: '../images/button_down.png',
            onClick: function () {
                colorBlind();
            }
        });
        viewer.addControl(button.element, { anchor: OpenSeadragon.ControlAnchor.TOP_LEFT });
        viewer.addControl(greyscaleButton.element, { anchor: OpenSeadragon.ControlAnchor.TOP_LEFT });
        if (zoom !== null && loc != null) {
            viewer.viewport.panTo(loc, true);
            viewer.viewport.zoomBy(zoom, loc, true);
        }
    }
    reload();
});

</script>
<template>
    <div>
        <!-- <div class="flex flex-row justify-center p-4 font-mono text-[24px] text-bold"> -->
        <div class="flex flex-row items-center">
        <nuxt-link to="/" class="px-4 py-5 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
            Patient Directory
        </nuxt-link>
        <h1 class="justify-center p-4 header-bar pl-5">Path-o-gen</h1>
        </div>


        <div>
            <div id="openseadragon1" class="px-12 h-screen"></div>
        </div>
    </div>
</template>
