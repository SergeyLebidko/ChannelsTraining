function validateString(str) {
    if (str.trim() === '') return false;

    const digits = '0123456789';
    if (digits.includes(str[0])) return false;

    const allowLetters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_' + digits;
    for (let letter of str) {
        if (!allowLetters.includes(letter)) return false;
    }

    return true;
}