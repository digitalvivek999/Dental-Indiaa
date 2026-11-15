/**
 * =========================================================================
 * ⚙️ CLIENT_CONFIG: WHITE-LABEL DENTAL CLIENT CONFIGURATION FILE
 * =========================================================================
 * To customize this entire website for a new client / dentist:
 * Simply update the values below! The entire website (phone, WhatsApp,
 * doctor name, address, Google Maps, ratings, reviews, SEO tags, schema)
 * will update AUTOMATICALLY across all sections in 10 seconds!
 * =========================================================================
 */

const SITE_CONFIG = {
  // 🏥 CLINIC BRANDING
  clinicName: "Apex Multispeciality Dental Clinic",
  clinicTagline: "Centre for Advanced Implantology & Cosmetic Dentistry",
  clinicLogoText: "APEX DENTAL",
  
  // 👨‍⚕️ DOCTOR PROFILE & CREDENTIALS
  doctorName: "Dr. Vivek Kumar Garg",
  doctorDegrees: "BDS, MDS (Prosthodontics & Oral Implantology)",
  doctorTitle: "Chief Clinical Director & Senior Implantologist",
  doctorExperienceYears: "14+",
  doctorBio: "A healthy, radiant smile is not a luxury — it is a basic human confidence right. We combine gentle, ethical healthcare with world-class digital dentistry so you never have to fear visiting a dentist again.",
  doctorPhoto: "images/doctor.jpg",
  
  // 📞 CONTACT & WHATSAPP
  phone: "+91 98765 43210",
  phoneRaw: "919876543210", // No spaces or symbols for tel: and wa.me
  whatsappNumber: "919876543210",
  whatsappDefaultMsg: "Hi Doctor, I would like to book an appointment for dental consultation.",
  email: "care@apexdentalclinic.in",
  
  // 📍 CLINIC LOCATION & GOOGLE BUSINESS (GMB)
  address: "Central Market, Metro Pillar 42, Connaught Place",
  city: "New Delhi",
  state: "Delhi NCR",
  pincode: "110001",
  country: "India",
  gmbReviewUrl: "https://search.google.com/local/writereview?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4",
  googleMapsEmbedUrl: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14008.114827187123!2d77.2144!3d28.6328!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390cfd37b04313f1%3A0x6b77c385c7827878!2sConnaught%20Place%2C%20New%20Delhi%2C%20Delhi!5e0!3m2!1sen!2sin!4v1680000000000!5m2!1sen!2sin",
  
  // ⭐ REVIEWS & RATINGS
  googleRating: "4.9",
  googleReviewCount: "1,450+",
  happyPatientsCount: "15,000+",
  
  // 🕒 TIMINGS & AVAILABILITY
  opdTimings: "Mon-Sat: 10:00 AM - 8:30 PM | Sun: By Appointment",
  morningSlot: "10:00 AM - 1:30 PM",
  eveningSlot: "5:00 PM - 8:30 PM",
  emergencyHelpline: "24/7 Dental Emergency Helpline",
  
  // 💰 CURRENCY & PRICING
  currencySymbol: "₹",
  rctPrice: "₹2,499",
  alignersPrice: "₹34,999",
  alignersEmi: "₹2,999/mo",
  implantsPrice: "₹18,999",
  whiteningPrice: "₹4,499",
  veneersPrice: "₹4,999",
  consultationPrice: "₹499",
  
  // 🌐 DOMAIN & SEO
  siteUrl: "https://dental-indiaa.netlify.app",
  metaTitle: "Apex Multispeciality Dental Clinic | Pain-Free Dentistry & Implants",
  metaDescription: "Premier multispeciality dental clinic in India. Advanced single-sitting painless RCT, German dental implants with lifetime warranty, and clear invisible aligners by MDS specialists."
};

// Export for module use or browser global
if (typeof module !== 'undefined' && module.exports) {
  module.exports = SITE_CONFIG;
}
