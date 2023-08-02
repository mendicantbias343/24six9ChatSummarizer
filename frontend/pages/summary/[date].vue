<template>
  <div class="flex flex-col justify-center items-start px-3 w-full">
    <Navigation :next_date="next_date" :previous_date="previous_date" 
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

      <ul class="pl-5">
        <li
          v-for="link in data.links"
          class="mt-3 text-primary underline underline-offset-2 list-disc"
        >
          <a
            v-if="typeof data.links[0] === 'object'"
            v-bind:href="link.link"
            target="_blank"
          >
            {{ link.link.slice(0, 35) }}...
          </a>
          <a v-else v-bind:href="link" target="_blank">
            {{ link.slice(0, 35) }}...</a
          >
        </li>
      </ul>
    </div>

    <div
      class="hiring-requests flex flex-col mt-10"
      v-if="data.hiring_requests.length != 0"
    >
      <h1 class="text-xl text-">Hiring Requests</h1>
      <ol class="pl-5 list-decimal">
        <li
          v-for="req in data.hiring_requests"
          class="w-full overflow-hidden mt-3 h-[2ch] text-accent-content list-decimal"
        >
          {{ req }}
        </li>
      </ol>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUpdated } from "vue";
import all_data from "../../content/final_data.json";
const route = useRoute();
const data = ref([]);
const other_data = all_data;
//extract all dates from the data
const dates = other_data.map((data) => data.date);
const count_of_dates = dates.length;
const current_index = dates.findIndex((x) => x == route.params.date);
import MarkdownIt from "markdown-it";
import { copyText } from 'vue3-clipboard'

const markdown = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
});
if (!route.params.date) {
  // we've to setup the first one as the main one
  data.value = all_data[all_data.length - 1];
} else {
  data.value = all_data.at(current_index);
}

function spliter(stringList) {
  return stringList.split(", ");
}

// navigation setup
const next_date = ref("");
const previous_date = ref("");
onUpdated(() => {
  next_date.value = "";
  previous_date.value = "";
});

if (current_index.value == 0) {
  // this is the earliest one
  previous_date.value = " ";
  next_date.value = dates[1];
} else if (current_index.value == count_of_dates - 1) {
  // this is the latest one
  previous_date.value = dates[count_of_dates - 2];
  next_date.value = " ";
} else {
  // we're in between somewhere
  previous_date.value = dates[current_index - 1];
  next_date.value = dates[current_index + 1];
}

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

// Example usage:
const inputDate = ref(route.params.date);
const formattedDate = ref(formatDate(inputDate.value));


</script>

<style>
.modal_description {
  word-wrap: break-word;
}

.modal_description  a {
  text-decoration: underline;
  color: #3c00c7
}



</style>
