export const generate_confirmation_code = () => {
  const length = 6;
  const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  let confirmationCode = "";
  for (let i = 0; i < length; i++) {
    const rand = Math.floor(Math.random() * characters.length);
    confirmationCode += characters[rand];
  }
  return confirmationCode;
};
