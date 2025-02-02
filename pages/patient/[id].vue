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

/* Dark Mode */
body.dark-mode {
    background-color: #333;
    color: white;
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
}

.dark-mode-button:hover {
    background-color: #555;
}
</style>

<script lang="ts">
export default {
    data() {
        return {
            darkMode: false
        };
    },
    methods: {
        toggleDarkMode() {
            this.darkMode = !this.darkMode;
            document.body.classList.toggle("dark-mode", this.darkMode);
        }
    }
};

import type OpenSeadragon from 'openseadragon';

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

                if (overlayVisible) {
                    request_string = 'http://127.0.0.1:5000/transform?' + new URLSearchParams({
                        url: request_string
                    });
                }

                return request_string;
            }
        }
    };

    let viewer: OpenSeadragon.Viewer | null = null;

    function reload() {
        let zoom: any | null = null;
        let loc: any | null = null;
        if (viewer !== null) {
            viewer.destroy();
            zoom = viewer.viewport.getZoom();
            loc = viewer.viewport.getCenter();
        }
        viewer = OpenSeadragon.default(options);
        const button = new OpenSeadragon.Button({
            tooltip: 'toggle heatmap',
            srcRest: 'images/button_rest.png',
            srcHover: 'images/button_hover.png',
            srcDown: 'images/button_down.png',
            onClick: function () {
                overlayVisible = !overlayVisible;
                reload();
            }
        });
        const greyscaleButton = new OpenSeadragon.Button({
            tooltip: 'greyscale heatmap',
            srcRest: 'images/debug_rest.png',   
            srcHover: 'images/debug_hover.png', 
            srcDown: 'images/debug_down.png',   
            onClick: function () {
                console.log('Greyscale Button Clicked!');
                alert('Greyscale Button Clicked!');
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
        <div class="header-bar">
            <h1>Path-o-gen</h1>
        </div>

        <button @click="toggleDarkMode" class="dark-mode-button">Toggle Dark Mode</button>

        <div>
            <div id="openseadragon1" class="p-4 h-screen"></div>
        </div>
    </div>
</template>
