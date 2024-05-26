import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export const cn = (...inputs: ClassValue[]) => {
  return twMerge(clsx(inputs))
};


export const getTimeWords = (minutes: number): string => {
    const hours = Math.floor(minutes / 60);
    const remainingMinutes = minutes % 60;

    const hourWord = getHourWord(hours);
    const minuteWord = getMinuteWord(remainingMinutes);

    if (hours > 0 && remainingMinutes == 0) return `${hours} ${hourWord}`;
    if (hours > 0) return `${hours} ${hourWord} ${remainingMinutes} ${minuteWord}`;
    return `${remainingMinutes} ${minuteWord}`;
};

export const getHourWord = (hours: number): string => {
    const lastDigit = hours % 10;
    const lastTwoDigits = hours % 100;

    if (lastTwoDigits >= 11 && lastTwoDigits <= 19) return 'часов';

    switch (lastDigit) {
        case 1:
            return 'час';
        case 2:
        case 3:
        case 4:
            return 'часа';
        default:
            return 'часов';
    }
};

export const getMinuteWord = (minutes: number): string => {
    const lastDigit = minutes % 10;
    const lastTwoDigits = minutes % 100;

    if (lastTwoDigits >= 11 && lastTwoDigits <= 19) return 'минут';

    switch (lastDigit) {
        case 1:
            return 'минута';
        case 2:
        case 3:
        case 4:
            return 'минуты';
        default:
            return 'минут';
    }
};

export const getPortionsWord = (quantity: number): string => {
  const lastDigit = quantity % 10;
  const lastTwoDigits = quantity % 100;

  if (lastTwoDigits >= 11 && lastTwoDigits <= 19) return `${quantity} порций`;

  switch (lastDigit) {
      case 1:
          return `${quantity} порция`;
      case 2:
      case 3:
      case 4:
          return `${quantity} порции`;
      default:
          return `${quantity} порций`;
  }
};

