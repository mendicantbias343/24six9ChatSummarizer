<template>
  <div class="flex flex-col justify-center items-start px-3 w-full">
    <Navigation next_date="" :previous_date="previous_date" 
    :formattedDate = "formattedDate"></Navigation>
   
    <div class="topics-holder w-full mt-10">
      <h1 class="text-xl text-accent-content">Topics Discussed</h1>

      <div class="topic flex flex-col lg:grid lg:grid-cols-3 lg:gap-4">
        <!-- card start-->
        <TopicCard :main_topics="data.main_topics"></TopicCard>
        <!-- Card end-->
        <!-- Links Shared -->
      </div>
    </div>
    <div class="links-shared flex flex-col mt-10">
      <h1 class="text-xl text-accent-content">Links Shared</h1>
      <ul class="pl-2">
        <li
          v-for="link in data.links"
          class="w-full overflow-hidden mt-3 h-[2ch] text-primary underline underline-offset-2 list-disc"
        >
          <a v-bind:href="link" target="_blank">{{ link.slice(0, 35) }}...</a>
        </li>
      </ul>
    </div>

    <div
      class="hiring-requests flex flex-col mt-10"
      v-if="data.hiring_requests.length != 0"
    >
      <h1 class="text-xl text-accent-content">Hiring Requests</h1>
      <ul class="pl-2">
        <li
          v-for="req in data.hiring_requests"
          class="w-full overflow-hidden mt-3 h-[2ch] text-secondary"
        >
          {{ req }}
        </li>
      </ul>
    </div>
  </div>
  


</template>

<script setup>
import all_data from "../content/final_data.json";

const route = useRoute();
let { data } = await useAsyncData('export', () => queryContent('export').findOne())
let csvdata = data

if (!route.params.date) {
  // we've to setup the first one as the main one
  data = all_data[all_data.length - 1];
}

const previous_date = "/summary/" + all_data[all_data.length - 2].date;

// date shinanigans
function formatDate(inputDate) {
  // Parse the input date string into a JavaScript Date object
  const day = parseInt(inputDate.substring(0, 2), 10);
  const month = parseInt(inputDate.substring(2, 4), 10) - 1;
  const year = parseInt(inputDate.substring(4, 8), 10);
  const dateObj = new Date(year, month, day);

  // Create an array of suffixes for the date
  const suffixes = ["th", "st", "nd", "rd"];
  let suffix;
  if (day >= 11 && day <= 13) {
    suffix = "th";
  } else {
    suffix = suffixes[day % 10] || "th";
  }

  // Format the date into 'DD, dd th/st mmm yyyy'
  const options = {
    weekday: "short",
    day: "2-digit",
    month: "short",
    year: "numeric",
  };
  const formattedDate = dateObj.toLocaleDateString("en-US", options);

  // Replace the 'DD' with the full weekday name
  const fullWeekdayName = dateObj.toLocaleDateString("en-US", {
    weekday: "long",
  });
  const finalFormattedDate = formattedDate.replace("DD", fullWeekdayName);

  return finalFormattedDate.replace("th", suffix);
}

const inputDate = ref(data.date);
const formattedDate = ref(formatDate(inputDate.value));

function splitter(arrayorstring){
  if(Array.isArray(arrayorstring)){
    return arrayorstring
  }
  else{
    return arrayorstring.split(",")
  }
}



</script>

<style scoped></style>
