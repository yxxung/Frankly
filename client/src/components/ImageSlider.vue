<template>
  <div class="image-album">
    <div class="images">
      <img
        class="image"
        v-for="imageUrl in imageUrls"
        v-bind:key="imageUrl.index"
        v-bind:src="imageUrl"
      />
    </div>
    <div v-if="imageUrls.length > 1" class="image-circle-wrapper">
      <div
        class="image-circle"
        v-for="(imageUrl, index) in imageUrls"
        v-bind:key="imageUrl.index"
        v-bind:class="{ activeImg: index === curPos }"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "imageSlider",
  data() {
    return {
      curPos: 0,
      postion: 0,
      start_x: 0,
      end_x: 0,
      IMAGE_WIDTH: 0,
      images: null,
      imageUrls: [
        "https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/09/shutterstock_1151676383.jpg",
        "https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/09/shutterstock_1151632343.jpg",
        "https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/09/shutterstock_1429964489.jpg",
      ],
    };
  },
  computed: {
    getImageWidth: () => {
      const imgWidth = document.querySelector(".images").offsetWidth;
      return imgWidth;
    },
  },
  mounted: function () {
    this.IMAGE_WIDTH = this.getImageWidth;
    this.images = document.querySelector(".images");
    this.images.addEventListener("touchstart", this.touch_start);
    this.images.addEventListener("touchend", this.touch_end);
  },
  methods: {
    prev() {
      if (this.curPos > 0) {
        this.postion += this.IMAGE_WIDTH;
        this.images.style.transform = `translateX(${this.postion}px)`;
        this.curPos = this.curPos - 1;
      }
    },
    next() {
      if (this.curPos < this.imageUrls.length - 1) {
        this.postion -= this.IMAGE_WIDTH;
        this.images.style.transform = `translateX(${this.postion}px)`;
        this.curPos = this.curPos + 1;
      }
    },

    touch_start(event) {
      this.start_x = event.touches[0].pageX;
    },

    touch_end(event) {
      this.end_x = event.changedTouches[0].pageX;
      if (this.start_x > this.end_x) this.next();
      else this.prev();
    },
  },
};
</script>

<style scopped>
.image-album {
  width: 100%;
  height: auto;
  max-width: 540px;
  max-height: 300px;
  overflow: hidden;
}
.images {
  position: relative;
  display: flex;
  height: auto;
  transition: transform 0.5s;
}
.image {
  width: 100%;
  height: auto;
  max-width: 540px;
  max-height: 300px;
}
.image-circle-wrapper {
  display: flex;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -18px);
}
.image-circle {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: white;
  border: 1px solid #d2d2d2;
  margin-right: 12px;
}
.image-circle:last-child {
  margin-right: 0;
}
.image-circle.activeImg {
  background-color: #404040;
}
</style>