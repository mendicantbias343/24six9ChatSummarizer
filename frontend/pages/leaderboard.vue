<template>
  <div>
    <div class="overflow-x-auto">
      <div v-if="loading">
        <LeaderboardTable
          :data="table_data[0]"
          :total_messages="table_data[1]"
          :last_date="last_date"
          :start_date="shared_dates[0]"
          :end_date="shared_dates[1]"
          @table-update="updateTable"
          
        ></LeaderboardTable>
      </div>
    </div>

    <!-- {{  getMessageCountsInRange(csvdata.body,'2023-05-27','2023-06-30')  }} -->
  </div>
</template>

<script setup>
import leaderboard_data from "../content/leaderboard.json";

const table_data = ref();
const loading = ref(false);

const last_date = new Date(Object.keys(leaderboard_data).pop())

const shared_dates = ref()
shared_dates.value = await last7days()

async function getMessageCountsInRange(data, dateRangeStart, dateRangeEnd) {
  const summedList = {};
  let total_msgs = 0;
  if (typeof dateRangeEnd == "string") {
    dateRangeStart = new Date(dateRangeStart);
    dateRangeEnd = new Date(dateRangeEnd);
  }
  for (let date in data) {
    let datex = new Date(date);
    if (datex >= dateRangeStart && datex <= dateRangeEnd) {
      for (const phoneNumber in data[date]) {
        const messages_count = parseInt(data[date][phoneNumber][0]);
        const media_count = parseInt(data[date][phoneNumber][1]);
        if (summedList[phoneNumber]) {
          try {
            summedList[phoneNumber]["messages"] += messages_count;
            summedList[phoneNumber]["media"] += media_count;
          } catch {
            print("error");
          }
        } else {
          summedList[phoneNumber] = {
            messages: messages_count,
            media: media_count,
          };
        }
        total_msgs += messages_count;
      }
    }
  }

  const sortedData = Object.fromEntries(
    Object.entries(summedList).sort((a, b) => b[1].messages - a[1].messages)
  );
  return [sortedData, total_msgs];
}

table_data.value = await getMessageCountsInRange(
  leaderboard_data,
  shared_dates.value[0],
  shared_dates.value[1]
);

async function ytdDateRange() {
  let startDate = new Date(new Date().getFullYear(), 0, 1);
  let endDate = new Date();
  return [startDate, endDate];
}

async function thisMonthRange() {
  let today = new Date()
  //check if we have data in this month
  if( last_date.getMonth() == today.getMonth()){
    let startDate = new Date(today.getFullYear(), today.getMonth(), 1);
    return [startDate, today];
  }
  else{ // we're getting last month data
    let startDate = new Date(today.getFullYear(), today.getMonth() - 1, 1);
    return [startDate, today];
  }
  
}

async function last7days() {
  return [ new Date(last_date.getTime() - (7 * 24 * 60 * 60 * 1000)) , last_date]
}

async function updateTable(filterType) {
  let dates = []

  switch (filterType) {
    case "ytd":
      dates = await ytdDateRange();
      table_data.value = await getMessageCountsInRange(
        leaderboard_data,
        dates[0],
        dates[1]
      );
      shared_dates.value = dates
      console.log(shared_dates.value)
      break;
    case "thismonth":
      dates = await thisMonthRange();
      table_data.value = await getMessageCountsInRange(
        leaderboard_data,
        dates[0],
        dates[1]
      );
      shared_dates.value = dates
      console.log(shared_dates.value)
      break;
    case "7days":
      dates = await last7days();
      table_data.value = await getMessageCountsInRange(
        leaderboard_data,
        dates[0],
        dates[1]
      );
      shared_dates.value = dates
      console.log(shared_dates.value[0])
      break;
    default:
      break;
  }
}

loading.value = true;
</script>

<style lang="scss" scoped></style>
