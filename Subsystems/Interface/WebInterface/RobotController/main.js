
let NUM_PARTICLES = ( ( ROWS = 50 ) * ( COLS = 50 ) ),
    THICKNESS = Math.pow( 20, 2 ),
    SPACING = 0,
    MARGIN = 0, // Set the fixed margin value
    COLOR = 0,
    DRAG = 0.9,
    EASE = 0.5,
    circlecontainer,
    particle,
    canvas,
    mouse,
    list,
    ctx,
    tog,
    man,
    dx, dy,
    mx, my,
    d, t, f,
    a, b,
    i, n,
    w, h,
    p, s,
    r, c,
    isDragging = false;

particle = {
  vx: 0,
  vy: 0,
  x: 0,
  y: 0,
  c1: COLOR,
  c2: COLOR,
  c3: COLOR
};

function init() {
  console.log("resize");
  circlecontainer = document.getElementById( 'circlecontainer' );
  canvas = document.createElement( 'canvas' );
  coords = document.getElementById( 'coords' ); 
  ctx = canvas.getContext( '2d' );
  man = false;
  tog = true;
  
  list = [];

  // Set the fixed size and position of the circlecontainer
  circlecontainer.style.width = "150px";
  circlecontainer.style.height = "150px";
  circlecontainer.style.cursor = "pointer";
  circlecontainer.style.position = "absolute";
  circlecontainer.style.top = "450px";
  circlecontainer.style.left = "-20px";

  SPACING = (circlecontainer.offsetWidth - MARGIN * 2) / COLS;
  w = canvas.width = COLS * SPACING + MARGIN * 2;
  h = canvas.height = ROWS * SPACING + MARGIN * 2;
  
  for ( i = 0; i < NUM_PARTICLES; i++ ) {
    p = Object.create( particle );
    p.x = p.ox = MARGIN + SPACING * ( i % COLS );
    p.y = p.oy = MARGIN + SPACING * Math.floor( i / COLS );
    list[i] = p;
  }

  circlecontainer.addEventListener('mousedown', (event) => {
    isDragging = true;
    man = true;

    circlecontainer.addEventListener( 'mousemove', function(e) {
      bounds = circlecontainer.getBoundingClientRect();
      mx = e.clientX - bounds.left;
      my = e.clientY - bounds.top;      
    });

    circlecontainer.addEventListener('mouseup', () => {
      isDragging = false;
      man = false;
      circlecontainer.removeEventListener('mousemove', step)
    });
  });
  
  circlecontainer.appendChild( canvas );
}

function step() {
  if(tog){
    if ( !isDragging) {
      mx = 70;
      my = 70;
    }
      
    for ( i = 0; i < NUM_PARTICLES; i++ ) {
      p = list[i];
      d = ( dx = mx - p.x ) * dx + ( dy = my - p.y ) * dy;
      f = -THICKNESS / d+8;

      if ( d < THICKNESS ) {
        t = Math.atan2( dy, dx );
        p.vx += f * Math.cos(t);
        p.vy += f * Math.sin(t);
        p.c1 = 1; // color
        p.c2 = 77;
        p.c3 = 107;
      }
      else{       
        p.c1 = p.c2 = p.c3 = 100;
      }
      if(p.vx > 10 ){
            p.c2 =255;      
      }
      if( p.vy > 10){       
        p.c3 = 255;
      }

      p.x += ( p.vx *= DRAG ) + (p.ox - p.x) * EASE;
      p.y += ( p.vy *= DRAG ) + (p.oy - p.y) * EASE;
    }
    tog = false;
  } else {
    b = ( a = ctx.createImageData( w, h ) ).data;
    for ( i = 0; i < NUM_PARTICLES; i++ ) {
      p = list[i];
      b[n = ( ~~p.x + ( ~~p.y * w ) ) * 4] = p.c1, b[n+1] = p.c2, b[n+2] = p.c3, b[n+3] = 250;
    }

    ctx.putImageData( a, 0, 0 );
    tog = true;
  }

  requestAnimationFrame( step );
}
function rangeSlide(value) {
  document.getElementById('rangeValue').innerHTML = value;
}

init();
step();
