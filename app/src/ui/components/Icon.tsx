// Volis — icônes React Native (react-native-svg). Grille 24 px, trait 2 px, extrémités arrondies.
// Usage : <Icon name="package" size={22} color={theme.colors.text} />
import * as React from 'react';
import type { ColorValue } from 'react-native';
import Svg, { Path } from 'react-native-svg';

export const iconPaths = {
  'alert-triangle': 'M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0zM12 9v4M12 17h.01',
  'arrows-swap': 'M4 8h15l-4-4M20 16H5l4 4',
  'bank': 'M3 10 12 4l9 6M5 10v8M9 10v8M15 10v8M19 10v8M3 21h18',
  'bell': 'M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0',
  'bolt': 'M13 2 4 14h7l-1 8 9-12h-7z',
  'calendar': 'M5 5h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zM3 10h18M8 3v4M16 3v4',
  'camera': 'M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1zM12 16.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z',
  'card': 'M4 5h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zM2 10h20',
  'check': 'M20 6 9 17l-5-5',
  'chevron-down': 'm6 9 6 6 6-6',
  'chevron-left': 'm15 18-6-6 6-6',
  'chevron-right': 'm9 6 6 6-6 6',
  'clock': 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 2',
  'close': 'M18 6 6 18M6 6l12 12',
  'cookie': 'M21 12a9 9 0 1 1-9-9 3 3 0 0 0 3 3 3 3 0 0 0 3 3 3 3 0 0 0 3 3zM8.5 9h.01M10 15h.01M15 15h.01',
  'copy': 'M9 9h11v11H9zM5 15H4V4h11v1',
  'currency-dollar': 'M12 2v20M17 6.5c0-1.9-2.2-3-5-3s-5 1.3-5 3.5 2.5 3 5 3.5 5 1.4 5 3.5-2.2 3.5-5 3.5-5-1.2-5-3',
  'document': 'M6 2h9l5 5v15H6zM14 2v6h6M9 13h8M9 17h6',
  'drop': 'M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z',
  'edit': 'M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z',
  'external': 'M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5',
  'eye': 'M2.06 12.35a1 1 0 0 1 0-.7 10.75 10.75 0 0 1 19.88 0 1 1 0 0 1 0 .7 10.75 10.75 0 0 1-19.88 0M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6',
  'filter': 'M4 6h16M7 12h10M10 18h4',
  'gift': 'M3 8h18v4H3zM5 12v9h14v-9M12 8v13M12 8S10.5 3 8 3.8C6 4.5 7 8 12 8zm0 0s1.5-5 4-4.2C18 4.5 17 8 12 8z',
  'globe': 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9s1-6.5 3.5-9',
  'help-circle': 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.7M12 17h.01',
  'home': 'M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z',
  'id-card': 'M5 5h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zM9 13a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM5.5 17c.6-1.6 1.9-2.3 3.5-2.3s2.9.7 3.5 2.3M15 10h4M15 14h3',
  'image': 'M5 4h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM9 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM21 16l-5-5-9 9',
  'info-circle': 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 16v-4M12 8h.01',
  'key': 'M2.59 17.41A2 2 0 0 0 2 18.83V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.17a2 2 0 0 0 1.42-.59l.81-.81a6.5 6.5 0 1 0-4-4zM16.5 7.5h.01',
  'leaf': 'M5 21c0-9 5-15 15-16-1 10-7 15-15 16zM5 21l7-7',
  'lock': 'M7 11h10a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2zM8 11V7a4 4 0 0 1 8 0v4',
  'logout': 'M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9',
  'mail': 'M5 5h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zM3 7l9 6 9-6',
  'map': 'M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2zM9 4v16M15 6v14',
  'map-pin': 'M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12zM12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
  'message': 'M21 11.5a8.5 8.5 0 0 1-12.4 7.6L3.5 20.5l1.4-4.6A8.5 8.5 0 1 1 21 11.5z',
  'minus': 'M5 12h14',
  'package': 'M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8',
  'phone': 'M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2',
  'plane': 'M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z',
  'plus': 'M12 5v14M5 12h14',
  'qr-code': 'M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h2v2h-2zM18 14h2M14 18h2M18 18h2v2',
  'ruler': 'M3 17 17 3l4 4L7 21zM7 13l2 2M10 10l2 2M13 7l2 2',
  'search': 'M11 18a7 7 0 1 0 0-14 7 7 0 0 0 0 14zM20 20l-3.5-3.5',
  'send': 'M22 2 11 13M22 2l-7 20-4-9-9-4z',
  'share': 'M4 12v8h16v-8M12 3v13M7 8l5-5 5 5',
  'shield': 'M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1zM9 12l2 2 4-4',
  'shirt': 'M8 3 4 6l2 4 2-1v12h8V9l2 1 2-4-4-3c-.5 1.5-2 2.5-4 2.5S8.5 4.5 8 3z',
  'sliders': 'M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6',
  'sort': 'M7 4v16M3 16l4 4 4-4M17 20V4M13 8l4-4 4 4',
  'star': 'M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.3 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z',
  'trash': 'M3 6h18M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2M6 6l1 14a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1l1-14M10 11v6M14 11v6',
  'user': 'M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21a8 8 0 0 1 16 0',
  'wallet': 'M3 7a2 2 0 0 1 2-2h13v4M3 7v11a2 2 0 0 0 2 2h15V9H5a2 2 0 0 1-2-2zM16 14h.01',
  'weight': 'M6 8h12l2 12H4zM9 8a3 3 0 0 1 6 0',
  'wifi-off': 'M2 8.8a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M12 20h.01M3 3l18 18',
} as const;

export type IconName = keyof typeof iconPaths;
type Props = { name: IconName; size?: number; color?: ColorValue; strokeWidth?: number; accessibilityLabel?: string };

export function Icon({ name, size = 24, color = '#1E2A3A', strokeWidth = 2, accessibilityLabel }: Props) {
  const fill = name === 'star' ? color : 'none';
  return (
    <Svg width={size} height={size} viewBox="0 0 24 24" fill={fill} accessible={!!accessibilityLabel}
      accessibilityLabel={accessibilityLabel} accessibilityElementsHidden={!accessibilityLabel}>
      <Path d={iconPaths[name]} stroke={color} strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" />
    </Svg>
  );
}
export default Icon;
