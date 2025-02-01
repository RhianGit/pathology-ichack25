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
    overlayElement.style.padding = "10px";
    overlayElement.src = "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg";

    let overlayVisible = false;

    const button = new OpenSeadragon.Button({

        tooltip: '',
        srcRest: 'images/button_rest.png',
        srcHover: 'images/button_hover.png',
        srcDown: 'images/button_down.png',
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
            overlayVisible = !overlayVisible;
            }
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
