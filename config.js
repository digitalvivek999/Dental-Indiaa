/**
 * =========================================================================
 * ⚙️ CLIENT_CONFIG: DR. S. LATHASREE DENTAL CLINIC (HANAMKONDA)
 * =========================================================================
 */

const DEFAULT_CONFIG = {
  // 🏥 CLINIC BRANDING
  clinicName: "Dr. S. Lathasree Dental Clinic",
  clinicTagline: "Centre for Pain-Free Multispeciality & Cosmetic Dentistry",
  clinicLogoText: "DR. LATHASREE DENTAL",
  
  // 👨‍⚕️ DOCTOR PROFILE & CREDENTIALS
  doctorName: "Dr. S. Lathasree",
  doctorDegrees: "BDS, MDS (Cosmetic Dentistry & Oral Implantology)",
  doctorTitle: "Chief Dental Surgeon & Senior Implantologist",
  doctorExperienceYears: "5+",
  doctorBio: "A healthy, beautiful smile brings lifelong confidence. We provide gentle, ethical, and 100% pain-free dental care equipped with modern digital technology and sterilized hospital-grade hygiene.",
  doctorPhoto: "images/doctor.jpg",
  
  // 📞 CONTACT & WHATSAPP
  phone: "+91 93475 94646",
  phoneRaw: "919347594646",
  whatsappNumber: "919347594646",
  whatsappDefaultMsg: "Hi Dr. Lathasree, I want to book an appointment for dental consultation.",
  email: "care@drlathasreedental.com",
  
  // 📍 CLINIC LOCATION & GOOGLE BUSINESS (GMB)
  address: "5-11-532, Sri Sai Nilayam, Road No. 2B, KU Cross",
  city: "Hanamkonda",
  state: "Telangana",
  pincode: "506009",
  country: "India",
  gmbReviewUrl: "https://maps.google.com/?q=5-11-532,+Sri+Sai+Nilayam,+Road+No.+2B,+KU+Cross,+Hanamkonda",
  googleMapsEmbedUrl: "https://maps.google.com/maps?q=5-11-532,+Sri+Sai+Nilayam,+Road+No.+2B,+KU+Cross,+Hanamkonda,+Warangal&t=&z=16&ie=UTF8&iwloc=&output=embed",
  
  // ⭐ REVIEWS & RATINGS
  googleRating: "4.9",
  googleReviewCount: "850+",
  happyPatientsCount: "10,000+",
  
  // 🕒 TIMINGS & AVAILABILITY
  opdTimings: "Mon-Sat: 10:00 AM - 8:30 PM | Sun: By Appointment",
  emergencyHelpline: "24/7 Dental Emergency Helpline",
  
  // 💰 PRICING & TREATMENTS
  currencySymbol: "₹",
  rctPrice: "₹2,499",
  alignersPrice: "₹34,999",
  999/mo",
  implantsPrice: "₹18,999",
  whiteningPrice: "₹4,499",
  veneersPrice: "₹4,999",
  consultationPrice: "₹499"
};

function getDynamicConfig() {
  const params = new URLSearchParams(window.location.search);
  const cfg = Object.assign({}, DEFAULT_CONFIG);

  if (params.get("doctor")) cfg.doctorName = params.get("doctor");
  if (params.get("clinic")) {
    cfg.clinicName = params.get("clinic");
    cfg.clinicLogoText = params.get("clinic").toUpperCase().replace("CLINIC", "").replace("DENTAL", "DENTAL").trim();
  }
  if (params.get("logo")) cfg.clinicLogoText = params.get("logo");
  if (params.get("city")) cfg.city = params.get("city");
  if (params.get("address")) cfg.address = params.get("address");
  if (params.get("phone")) {
    const raw = params.get("phone").replace(/\D/g, "");
    cfg.phone = "+91 " + (raw.length === 10 ? raw : raw.slice(-10));
    cfg.phoneRaw = raw.length === 10 ? ("91" + raw) : raw;
    cfg.whatsappNumber = cfg.phoneRaw;
  }
  if (params.get("wa")) cfg.whatsappNumber = params.get("wa").replace(/\D/g, "");
  if (params.get("rating")) cfg.googleRating = params.get("rating");
  if (params.get("reviews")) cfg.googleReviewCount = params.get("reviews");

  return cfg;
}

const SITE_CONFIG = getDynamicConfig();
