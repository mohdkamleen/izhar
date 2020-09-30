var appVersion = '1.0';

var files = [
    './index.py',
    './project.py',
    './other.py',
    './contact.py',
    './a1.py',
    './a2.py',
    './a3.py',
    './a4.py',
    './a5.py', 
    './t1.py',
    './t2.py',
    './t3.py',
    './t4.py',
    './t5.py',
    './t6.py',
    './t7.py',
    './t8.py',
    './tp1.py',
    './other.py',
    './README.md',
    './css/dark.css',
    './css/style.css',
    './css/bootstraph.css',
    './css/kamleen.jpg',
    './css/resume.png',
    './css/download.jpg',
    './css/sound.mp3',
    './source/a1.txt',
    './source/a2.txt',
    './source/a3.txt',
    './source/a4.txt',
    './source/a5.txt',
    './source/t1.txt',
    './source/t2.txt',
    './source/t3.txt',
    './source/t4.txt',
    './source/t5.txt',
    './source/t5.1.py',
    './source/t5.2.py',
    './source/t5.3.py',
    './source/t5.4.py',
    './source/t5.5.py',
    './source/t4.1.py',
    './source/t4.2.py',
    './source/t4.3.py',
    './source/t2.3.py',
    './source/t1.1.py',
    './source/t1.2.py',
    './source/t1.3.py',
    './source/t8.2.py',
    './source/t7.1.py',
    './source/tp1.1.py',
    './source/tp1.2.py',
    './source/tp1.3.py',
    './source/tp1.4.py',
    './source/tp1.5.py',
    './script.js',
    './sw.js', 
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
    'https://1.bp.blogspot.com/-0pqQmwCrcWk/XzCVZUtkSWI/AAAAAAAABNY/v6wkJyj6THYYR1tVoYTm3HByigXkSQ_0gCLcBGAsYHQ/s2048/IMG_20200325_140110.jpg',
    'https://fonts.googleapis.com/css?family=Short+Stack&display=swap',
    'https://unpkg.com/sweetalert/dist/sweetalert.min.js',
    'https://www.gstatic.com/firebasejs/7.15.4/firebase.js'
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(appVersion)
        .then(cache => {
            return cache.addAll(files)
            .catch(err => {
                console.error('Error adding files to cache', err);
            })
        })
    )
    console.info('Service Worker is Installed');
    self.skipWaiting();
})


self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys()
        .then(cachename => {
            return Promise.all(
                cachename.map(cache => {
                    if(cache != appVersion){
                        console.info('delete old caches', cache)
                        return caches.delete(cache);
                    }
                })
              )
           })
         )
            return self.clients.claim();
        })


        self.addEventListener("fetch", event => {
            console.info('Service Worker fetch', event.request.url);
            event.respondWith(
                caches.match(event.request)
                .then(res => {
                    return res || fetch(event.request);
                })
            )
         })