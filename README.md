# Sanic Memory Leak

## Instruction
Build the docker image
`docker build --pull --rm -f "dockerfile" -t leak:latest "."`

Run the docker image
`docker run -p 8000:8000 leak:latest`

Open the application
http://localhost:8000/fe

Use docker desktop to have a look at the stats. And then simply force refresh the page to see the memory increase...

I hope this helps.