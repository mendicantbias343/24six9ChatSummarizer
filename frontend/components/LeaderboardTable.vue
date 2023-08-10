<template>
  <div>
    <h1 class="text-xl font-black ml-3">Top 10 Contributors</h1>
    <div class="w-full flex flex-row justify-end mt-5">
      <div class="mr-3 text-sm">Filter:</div>
      <div class="join join-horizontal lg:join-horizontal text-left">
        <input
          class="btn btn-xs active join-item normal-case mr-1"
          type="radio"
          name="options"
          aria-label="Year to date"
          @click="askForUpdate('ytd')"
        />
        <input
          class="btn btn-xs join-item normal-case mr-1"
          type="radio"
          name="options"
          aria-label="This Month"
          @click="askForUpdate('thismonth')"
        />
        <input
          class="btn btn-xs join-item normal-case"
          type="radio"
          checked
          name="options"
          aria-label="Last 7 Days"
          @click="askForUpdate('7days')"
        />
      </div>
      
    </div>
    <div class="filter-description text-xs opacity-50 mt-2 text-right">
        <span v-if="current_filter == '7days'">
          Showing last 7 days from  {{  getFormattedDate(start_date) }} to  {{  getFormattedDate(end_date) }}
        </span>
        <span v-if="current_filter == 'thismonth'">
          Showing this month from  {{  getFormattedDate(start_date) }} to  {{  getFormattedDate(end_date) }}
        </span>
        <span v-if="current_filter == 'ytd'">
          Showing the leaderboard for the year <span class=" font-bold">{{  end_date.getFullYear() }}</span> 
        </span>
      </div>
    
    <table class="table table-lg transition-all duration-500">
      <!-- head -->
      <thead>
        <tr>
          <th>Name</th>
          <th>Messages</th>
          <th class="hidden md:table-cell">Media Shared</th>
        </tr>
      </thead>
      <tbody>
        <!-- row 1 -->
        <tr
          v-for="(counts, ph) in Object.fromEntries(
            Object.entries(data).slice(0, 10)
          )"
        >
          <td>
            <div class="flex items-center space-x-3">
              <div class="avatar">
                <div class="mask mask-squircle w-12 h-12">
                  <img
                    src="https://i.pravatar.cc/300"
                    alt="Avatar Tailwind CSS Component"
                  />
                </div>
              </div>
              <div>
                <div class="font-bold">{{ ph }}</div>
              </div>
            </div>
          </td>
          <td class="w-32">
            <div class="flex flex-col gap-1">
              <div class="relative h-100 pl-1">
                {{ counts["messages"] }}
                <div
                  class="absolute top-0 left-0 bg-primary h-6 z-[-2] rounded-md"
                  :style="
                    'width:' + barWidth(counts['messages'], total_messages)
                  "
                >
                  &nbsp;
                </div>
              </div>
              <div
                class="flex flex-row items-center md:hidden text-xs opacity-60 gap-1"
              >
                Media: 
                <span class="opacity-100">
                  {{ counts["media"] }}
                </span>
              </div>
            </div>
          </td>
          <td class="w-32 hidden md:table-cell">
            {{ counts["media"] }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const props = defineProps({
  data: Object,
  total_messages: Number,
  last_date: Date,
  start_date: Date,
  end_date: Date
});



const emit = defineEmits(["table-update"]);

const { data, total_messages, start_date, end_date } = toRefs(props);


const curr_max_count = ref();

curr_max_count.value = Object.values(Object.values(data.value)[0])[0];

const current_filter = ref('7days')

function barWidth(count, total_messages) {
  curr_max_count.value = Object.values(Object.values(data.value)[0])[0];
  return Math.round((count * 100) / curr_max_count.value) + "%";
}

async function askForUpdate(filterType) {
  emit('table-update', filterType)
  current_filter.value = filterType
}

function dateToString(date){
  return date.toDateString
}

function getFormattedDate(date) {
  var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  var year = date.getFullYear();

  var month = date.getMonth()
  month = months[month]

  var day = date.getDate().toString();
  day = day.length > 1 ? day : '0' + day;
  
  return day + ' ' + month ;
}

</script>

<style lang="scss" scoped></style>
