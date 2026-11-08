function spriteSVG(kind, outfit){
  const C = {
    leo:   {fill:"#F4A261", accent:"#E76F51", feature:"mane"},
    zara:  {fill:"#F8F9FA", accent:"#212529", feature:"stripes"},
    momo:  {fill:"#A98467", accent:"#D4A373", feature:"ears"},
    pip:   {fill:"#E76F51", accent:"#F4A261", feature:"beak"},
    tiko:  {fill:"#F4A261", accent:"#1a1a2e", feature:"tiger"},
    nala:  {fill:"#E9C46A", accent:"#A98467", feature:"spots"},
    bongo: {fill:"#9CA3AF", accent:"#6B7280", feature:"hippo"}
  };
  const c = C[kind] || C.leo;
  let extras = "";
  let face = "";
  const eyes = `<ellipse cx="28" cy="36" rx="10" ry="11" fill="#fff"/><ellipse cx="52" cy="36" rx="10" ry="11" fill="#fff"/><circle cx="30" cy="37" r="4" fill="#1a1a2e"/><circle cx="54" cy="37" r="4" fill="#1a1a2e"/>`;

  if(kind==="leo"){
    extras = `<path d="M12 28 Q8 12 20 18" fill="${c.accent}"/><path d="M68 28 Q72 12 60 18" fill="${c.accent}"/><path d="M20 14 Q40 4 60 14" fill="${c.accent}"/><circle cx="18" cy="22" r="6" fill="${c.accent}"/><circle cx="62" cy="22" r="6" fill="${c.accent}"/>`;
    face = eyes + `<ellipse cx="40" cy="52" rx="8" ry="5" fill="${c.accent}"/><circle cx="40" cy="50" r="2.5" fill="#1a1a2e"/>`;
  } else if(kind==="zara"){
    extras = `<rect x="18" y="14" width="5" height="18" fill="${c.accent}"/><rect x="28" y="12" width="5" height="20" fill="${c.accent}"/><rect x="47" y="12" width="5" height="20" fill="${c.accent}"/><rect x="57" y="14" width="5" height="18" fill="${c.accent}"/>`;
    face = eyes + `<ellipse cx="40" cy="52" rx="7" ry="4" fill="#DEE2E6"/><ellipse cx="40" cy="51" rx="2" ry="1.5" fill="#1a1a2e"/>`;
  } else if(kind==="momo"){
    extras = `<ellipse cx="14" cy="28" rx="8" ry="10" fill="${c.fill}"/><ellipse cx="66" cy="28" rx="8" ry="10" fill="${c.fill}"/><ellipse cx="14" cy="28" rx="4" ry="5" fill="${c.accent}"/><ellipse cx="66" cy="28" rx="4" ry="5" fill="${c.accent}"/>`;
    face = eyes + `<ellipse cx="40" cy="50" rx="12" ry="10" fill="${c.accent}"/><ellipse cx="40" cy="52" rx="4" ry="3" fill="#1a1a2e"/>`;
  } else if(kind==="pip"){
    extras = `<path d="M16 22 Q40 6 64 22" fill="${c.fill}"/><path d="M8 40 Q4 50 14 48" fill="${c.fill}"/><path d="M72 40 Q76 50 66 48" fill="${c.fill}"/>`;
    face = eyes + `<path d="M34 48 L40 62 L46 48 Z" fill="#F4A261"/>`;
  } else if(kind==="tiko"){
    extras = `<path d="M18 18 L24 8 L30 18" fill="${c.fill}" stroke="${c.accent}" stroke-width="1"/><path d="M50 18 L56 8 L62 18" fill="${c.fill}" stroke="${c.accent}" stroke-width="1"/><path d="M22 44 L26 58" stroke="${c.accent}" stroke-width="3"/><path d="M40 42 L40 60" stroke="${c.accent}" stroke-width="3"/><path d="M54 44 L50 58" stroke="${c.accent}" stroke-width="3"/>`;
    face = eyes + `<ellipse cx="40" cy="52" rx="8" ry="5" fill="#FEFAE0"/><ellipse cx="40" cy="51" rx="2.5" ry="2" fill="#1a1a2e"/>`;
  } else if(kind==="nala"){
    extras = `<rect x="36" y="2" width="8" height="16" rx="3" fill="${c.fill}"/><circle cx="28" cy="48" r="4" fill="${c.accent}" opacity=".7"/><circle cx="52" cy="50" r="3.5" fill="${c.accent}" opacity=".7"/><circle cx="40" cy="58" r="3" fill="${c.accent}" opacity=".7"/><ellipse cx="18" cy="16" rx="4" ry="5" fill="${c.accent}"/><ellipse cx="62" cy="16" rx="4" ry="5" fill="${c.accent}"/>`;
    face = `<ellipse cx="28" cy="32" rx="9" ry="10" fill="#fff"/><ellipse cx="52" cy="32" rx="9" ry="10" fill="#fff"/><circle cx="30" cy="33" r="3.5" fill="#1a1a2e"/><circle cx="54" cy="33" r="3.5" fill="#1a1a2e"/><ellipse cx="40" cy="48" rx="6" ry="4" fill="${c.fill}"/><ellipse cx="40" cy="47" rx="2" ry="1.5" fill="#1a1a2e"/>`;
  } else {
    extras = `<ellipse cx="14" cy="24" rx="7" ry="5" fill="${c.accent}"/><ellipse cx="66" cy="24" rx="7" ry="5" fill="${c.accent}"/>`;
    face = eyes + `<ellipse cx="40" cy="54" rx="14" ry="10" fill="#D1D5DB"/><ellipse cx="32" cy="54" rx="3" ry="2" fill="#1a1a2e"/><ellipse cx="48" cy="54" rx="3" ry="2" fill="#1a1a2e"/>`;
  }

  let hat="",acc="";
  if(outfit==="crown") hat=`<path d="M24 12 L30 2 L40 10 L50 2 L56 12 Z" fill="#E9C46A" stroke="#B08900" stroke-width="1"/>`;
  if(outfit==="shades") acc=`<rect x="18" y="30" width="44" height="12" rx="3" fill="#1a1a2e"/>`;
  if(outfit==="disco") acc=`<circle cx="22" cy="58" r="3" fill="#ff6b6b"/><circle cx="40" cy="62" r="3" fill="#48dbfb"/><circle cx="58" cy="58" r="3" fill="#feca57"/>`;
  if(outfit==="tuxedo") acc=`<rect x="28" y="58" width="24" height="14" fill="#1a1a2e"/><rect x="34" y="58" width="12" height="6" fill="#fff"/>`;
  if(outfit==="cape") acc=`<path d="M16 50 L8 78 L40 62 L72 78 L64 50" fill="#E76F51" opacity=".8"/>`;
  if(outfit==="hula") acc=`<ellipse cx="40" cy="68" rx="22" ry="5" fill="#2A9D8F"/>`;
  if(outfit==="space") hat=`<ellipse cx="40" cy="14" rx="26" ry="14" fill="#dee2e6" stroke="#adb5bd" stroke-width="2"/>`;
  if(outfit==="chef") hat=`<rect x="26" y="2" width="28" height="12" rx="4" fill="#fff"/><rect x="22" y="12" width="36" height="6" rx="2" fill="#fff"/>`;
  if(outfit==="rain") acc=`<path d="M14 48 L40 42 L66 48 L62 72 L18 72 Z" fill="#48dbfb" opacity=".45"/>`;

  const body = `
    <rect class="arm-l" x="6" y="70" width="12" height="22" rx="6" fill="${c.fill}"/>
    <rect class="arm-r" x="62" y="70" width="12" height="22" rx="6" fill="${c.fill}"/>
    <rect x="22" y="68" width="36" height="28" rx="8" fill="${c.fill}"/>
    <rect class="leg-l" x="24" y="94" width="12" height="14" rx="5" fill="${c.fill}"/>
    <rect class="leg-r" x="44" y="94" width="12" height="14" rx="5" fill="${c.fill}"/>
  `;

  return `<svg class="sprite" viewBox="0 0 80 110" xmlns="http://www.w3.org/2000/svg">
    <g class="figure">
      ${body}
      ${acc}
      <rect x="12" y="16" width="56" height="54" rx="14" fill="${c.fill}"/>
      ${extras}
      ${face}
      ${hat}
    </g>
  </svg>`;
}
