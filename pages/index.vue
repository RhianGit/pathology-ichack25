<style>
.header-bar {
    padding: 10px;
    text-align: center;
    font-family: 'Courier New', Courier, monospace;
    font-size: 24px;
    font-weight: bold;
}

body {
    background-color: #F2F2EB;
    /* Light grey background */
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
</style>

<script lang="ts">
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

                console.log("h");

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

                return request_string;
            }
        }
    });
    const overlayElement = document.createElement("img");
    overlayElement.id = "example-overlay";
    overlayElement.src = "https://upload.wikimedia.org/wikipedia/commons/1/1d/Captura_de_tela_2024-12-19_224037.png";
    // overlayElement.style.width = `${slide_width}`;
    // overlayElement.style.height = `${slide_height}`;
    overlayElement.style.opacity = "0.5";

    let overlayVisible = false;

    const button = new OpenSeadragon.Button({

        tooltip: '',
        srcRest: 'images/button_rest.png',
        srcHover: 'images/button_hover.png',
        srcDown: 'images/button_down.png',
        onClick: function () {
            if (overlayVisible) {
                viewer.removeOverlay('example-overlay');
            } else {
                viewer.addOverlay({
                    element: overlayElement,
                    location: new OpenSeadragon.Point(0, 0),
                    width: slide_width,
                    height: slide_height,
                    checkResize: true,
                });

            }
            overlayVisible = !overlayVisible;
        }
    });

    viewer.addControl(button.element, { anchor: OpenSeadragon.ControlAnchor.TOP_LEFT });
});

</script>

<template>
    <div>
        <div class="header-bar">
            <h1>Pathology heatmap generator</h1>
        </div>

        <div>
            <div id="openseadragon1" class="p-4 h-screen"></div>
        </div>
    </div>
</template>
