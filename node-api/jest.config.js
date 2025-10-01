// jest.config.js
export default {
  transform: {},                // disables Babel transforms, needed for native ESM support
//   extensionsToTreatAsEsm: ['.js'],  // treat .js files as ESM
  testEnvironment: 'node'       // Node.js environment for tests
};
