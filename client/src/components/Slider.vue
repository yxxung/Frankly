<template>
  <vueper-slides
    class="no-shadow"
    :visible-slides="3"
    :arrows="false"
    :slide-ratio="1 / 4"
    :gap="4"
    :dragging-distance="50"
    :bullets="false"
    :slideImageInside="true"
    >
    <vueper-slide v-for="(slide, i) in slides"
                  :key="i"
                  :image="slide.image"
                  :link="slide.link"/>
  </vueper-slides>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides';
import 'vueperslides/dist/vueperslides.css';
export default {
  name: 'Slider',
  components: {
    'VueperSlides': VueperSlides,
    'VueperSlide': VueperSlide,
  },
  data: () => ({
    slides: [
      { image: require('@/assets/party/국민의힘.svg'),
        link: 'https://www.peoplepowerparty.kr/intro.jsp'},
      { image: require('@/assets/party/기본소득당.svg'),
        link: 'https://www.basicincomeparty.kr/'},
      { image: require('@/assets/party/더불어민주당.svg'),
        link: 'https://theminjoo.kr/'},
      { image: require('@/assets/party/시대전환.svg'),
        link: 'https://www.transition.kr/home/'},
      { image: require('@/assets/party/정의당.svg'),
        link: 'https://www.justice21.org/newhome/main/default.html'},
    ]
  })
}
</script>

<style>
.vueper-slides {
  padding: 8px 24px;
}
.vueperslide {
  top: 10px;
  background: #FFFFFF;
  box-shadow: 0px 2px 14px rgba(0, 0, 0, 0.12);
  height: 96px;
  width: 144px;
  margin: 0 auto;
}
</style>
