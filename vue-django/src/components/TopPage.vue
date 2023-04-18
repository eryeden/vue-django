<script>

import axios from "axios"

export default{
    name: "TopPage",
    props: {
        msg: String,
    },
    data() {
        return {
            text: null,
        }
    },
    mounted(){
        axios.get("/api/v1/sample").then(
            (response) => (this.text = response.data)
        ).catch(
            (e) => console.log(e)
        );
    },
}

</script>

<template>
    <h2>TopPage</h2>
    <h1>{{msg}}</h1>
    <div>{{text}}</div>
</template>

<style scoped>
h1 {
    font-weight: 500;
    font-size: 2.6rem;
    top: -10px;
}

h3 {
    font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
    text-align: center;
}

@media (min-width: 1024px) {

    .greetings h1,
    .greetings h3 {
        text-align: left;
    }
}
</style>
