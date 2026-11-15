/**
 * =========================================================================
 * 🚀 DYNAMIC URL-BASED PERSONALIZATION ENGINE (MAGIC PITCH LINKS)
 * =========================================================================
 * How this works:
 * If you send a link with query parameters like:
 * ?doctor=Dr.+Amit+Verma&clinic=Verma+Dental+Clinic&city=Mumbai&phone=9876543210
 * 
 * The website will AUTOMATICALLY render in that dentist's name, clinic,
 * city, and phone number WITHOUT editing ANY code!
 * =========================================================================
 */

const DEFAULT_CONFIG = {
  clinicName: "Apex Multispeciality Dental Clinic",
  clinicTagline: "Centre for Advanced Implantology & Cosmetic Dentistry",
  clinicLogoText: "APEX DENTAL",
  doctorName: "Dr. Vivek Kumar Garg",
  doctorDegrees: "BDS, MDS (Prosthodontics & Oral Implantology)",
  doctorTitle: "Chief Clinical Director & Senior Implantologist",
  doctorExperienceYears: "14+",
  doctorBio: "A healthy, radiant smile is not a luxury — it is a basic human confidence right. We combine gentle, ethical healthcare with world-class digital dentistry so you never have to fear visiting a dentist again.",
  doctorPhoto: "images/doctor.jpg",
  phone: "+91 98765 43210",
  phoneRaw: "919876543210",
  whatsappNumber: "919876543210",
  whatsappDefaultMsg: "Hi Doctor, I would like to book an appointment for dental consultation.",
  email: "care@apexdentalclinic.in",
  address: "Central Market, Metro Pillar 42, Connaught Place",
  city: "New Delhi",
  state: "Delhi NCR",
  pincode: "110001",
  country: "India",
  gmbReviewUrl: "https://search.google.com/local/writereview?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4",
  googleMapsEmbedUrl: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14008.114827187123!2d77.2144!3d28.6328!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390cfd37b04313f1%3A0x6b77c385c7827878!2sConnaught%20Place%2C%20New%20Delhi%2C%20Delhi!5e0!3m2!1sen!2sin!4v1680000000000!5m2!1sen!2sin",
  googleRating: "4.9",
  googleReviewCount: "1,450+",
  happyPatientsCount: "15,000+",
  opdTimings: "Mon-Sat: 10:00 AM - 8:30 PM | Sun: By Appointment",
  emergencyHelpline: "24/7 Dental Emergency Helpline",
  currencySymbol: "₹",
  rctPrice: "₹2,499",
  alignersPrice: "₹34,999",
  alignersEmi: "₹2,999/mo",
  implantsPrice: "₹18,999",
  whiteningPrice: "₹4,499",
  veneersPrice: "₹4,999",
  consultationPrice: "₹499"
};

// Function to read URL parameters and override default config
function getDynamicConfig() {
  const params = new URLSearchParams(window.location.search);
  const cfg = Object.assign({}, DEFAULT_CONFIG);

  if (params.get("doctor")) {
    cfg.doctorName = params.get("doctor");
  }
  if (params.get("clinic")) {
    cfg.clinicName = params.get("clinic");
    cfg.clinicLogoText = params.get("clinic").toUpperCase().replace("CLINIC", "").replace("DENTAL", "DENTAL").trim();
  }
  if (params.get("logo")) {
    cfg.clinicLogoText = params.get("logo");
  }
  if (params.get("city")) {
    cfg.city = params.get("city");
  }
  if (params.get("address")) {
    cfg.address = params.get("address");
  }
  if (params.get("phone")) {
    const raw = params.get("phone").replace(/\D/g, "");
    cfg.phone = "+91 " + (raw.length === 10 ? raw : raw.slice(-10));
    cfg.phoneRaw = raw.length === 10 ? ("91" + raw) : raw;
    cfg.whatsappNumber = cfg.phoneRaw;
  }
  if (params.get("wa")) {
    cfg.whatsappNumber = params.get("wa").replace(/\D/g, "");
  }
  if (params.get("rating")) {
    cfg.googleRating = params.get("rating");
  }
  if (params.get("reviews")) {
    cfg.googleReviewCount = params.get("reviews");
  }
  if (params.get("degrees")) {
    cfg.doctorDegrees = params.get("degrees");
  }
  if (params.get("exp")) {
    cfg.doctorExperienceYears = params.get("exp");
  }

  // Update dynamic meta title if custom clinic/doctor
  if (params.get("clinic") || params.get("doctor")) {
    cfg.metaTitle = `${cfg.clinicName} | ${cfg.doctorName} | Pain-Free Dental Care`;
  }

  return cfg;
}

const SITE_CONFIG = getDynamicConfig();
