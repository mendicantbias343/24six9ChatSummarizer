<template>
    <div class="flex flex-col items-center mx-auto lg:w-[1000px]">
        <header class=" bg-base-100 w-full text-center px-2 text-secondary flex flex-row justify-around align-middle items-center mb-5 lg:w-96">
            <img class="w-20 m-5 aspect-square object-contain rounded-full border-spacing-1 border-b-slate-500 " src="../assets/img/main_logo.jpg" >
           <span class="block text-xl text-left text-info ">Founders Community Whatsapp Summary</span>
            

        </header>
        <slot />

        <footer class="bg-black w-full text-center p-5 mt-10 text-secondary flex flex-row justify-around align-middle items-center shadow-xl ">
            <div>
                Made with ❤️ by  <a href="https://rkakodker.com" class=" underline underline-offset-4"> Rameez Kakodker</a>
            </div>
        </footer>
    </div>
</template>
