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
    async function handleFormSubmit() {
        try {
            const response = await fetch('http://127.0.0.1:5000/transform?' + new URLSearchParams({
                url: "https://slides.virtualpathology.leeds.ac.uk/Research_1/Prof_Quirke/TISSUE_BANK/GIFT_16/17229.svs?512+1536+512+512+16+100"
            }), {
                method: 'GET',
                mode: 'cors',
                credentials: 'omit'
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const imageBlob = await response.blob();
            const imageUrl = URL.createObjectURL(imageBlob);

            const overlayElement = document.getElementById('example-overlay'); // Assuming there's an element with this ID
            if (overlayElement) {
                overlayElement.src = imageUrl;
                overlayElement.style.width = "100%";
                overlayElement.style.height = "100%";
                console.log(overlayElement.src);
            } else {
                console.error('Overlay element not found');
            }
        } catch (error) {
            console.error('Error fetching or processing the image:', error);
        }
    }

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
                handleFormSubmit();
                viewer.addOverlay({
                    element: overlayElement,
                    location: new OpenSeadragon.Rect(0, 0, 1, 1),
                    width: slide_width,
                    height: slide_height,
                    checkResize: false,
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
